from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NotificationForm

# Create your views here.
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

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user)
        notification_form = NotificationForm(request.POST, instance=user)

        if profile_form.is_valid() and notification_form.is_valid():
            profile_form.save()
            notification_form.save()
            return redirect('settings')  # 保存後重新導向到設定頁面

    else:
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
            return redirect('settings')  # 重定向到設定頁面
    else:
        profile_form = ProfileForm(instance=user)

    context = {
        'profile_form': profile_form,
    }

    return render(request, 'settings.html', context)

@login_required
def update_notification(request):
    user = request.user
    notification_settings = user

    if request.method == 'POST':
        notification_form = NotificationForm(request.POST, instance=notification_settings)
        if notification_form.is_valid():
            notification_form.save()
            return redirect('settings')  # 重定向到設定頁面
    else:
        notification_form = NotificationForm(instance=notification_settings)

    context = {
        'notification_form': notification_form,
    }

    return render(request, 'settings.html', context)