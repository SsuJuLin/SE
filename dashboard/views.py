from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NotificationForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def sales_line_chart_data(request):
    # Implement the logic to retrieve the sales data
    sales_data = [1000, 1500, 2000, 1200, 1800, 2500, 3000, 4200, 2000, 1500, 2500, 3000]
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Oct', 'Nov', 'Dec']

    data = {
        'labels': labels,
        'data': sales_data
    }
    
    return JsonResponse(data)

def dashboard(request):
    return render(request, 'dashboard.html')

def sales_chart_data(request):
    # 實現銷售圖表數據的邏輯
    data = {
        "labels": ["Category 1", "Category 2", "Category 3"],
        "data": [50, 30, 20]
    }
    return JsonResponse(data)

def stock_chart_data(request):
    # 實現產品庫存圖表數據的邏輯
    data = {
        "labels": ["Category 1", "Category 2", "Category 3"],
        "data": [10, 20, 30]
    }
    return JsonResponse(data)

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
            print(profile_form.errors)
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