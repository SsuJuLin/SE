from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProfileForm, NotificationForm,RegistrationForm


# Create your views here.
class SignUp_View(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def signup(request):
    user = request.user
    if request.method == 'POST':
        form = RegistrationForm(request.POST,instance=user)
        if form.is_valid():
            # 檢查使用者名稱是否已存在
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, '該使用者名稱已被使用。請選擇其他使用者名稱。')
            else:
                print(form.errors)
                form.save()
                messages.success(request, '註冊成功！')
                return redirect('home')
        else:
            print(form.errors)
            messages.error(request, '註冊失敗。請檢查輸入內容。')
    else:
        print(form.errors)
        form = RegistrationForm(instance=user)

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard_view(request):
    # 在這裡處理從後端獲取數據等相關邏輯
    context = {
        # 將需要傳遞到模板中的變數添加到context字典中
        'total_sales': 10000,
        'best_selling_product': 'Product A',
        # 其他變數...
    }
    return render(request, 'dashboard.html', context)

@login_required
def settings_view(request):
    user = request.user

    profile_form = ProfileForm(instance=user)
    notification_form = NotificationForm(instance=user)

    context = {
        'profile_form': profile_form,
        'notification_form': notification_form,
    }

    return render(request, 'settings.html', context)

@login_required
def update_profile(request):
    user = request.user

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "成功更新個人資料。")
        else:
            messages.error(request, "無法更新個人資料。")
    else:
        profile_form = ProfileForm(instance=user)

    context = {
        'profile_form': profile_form,
    }

    return render(request, 'settings.html', context)

@login_required
def update_notifications(request):
    user = request.user

    if request.method == 'POST':
        notification_form = NotificationForm(request.POST, instance=user)
        if notification_form.is_valid():
            notification_form.save()
            messages.success(request, "成功更新通知設定。")
        else:
            messages.error(request, "無法更新通知設定。")
    else:
        notification_form = NotificationForm(instance=user)

    context = {
        'notification_form': notification_form,
    }

    return render(request, 'settings.html', context)