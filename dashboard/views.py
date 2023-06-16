from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProfileForm, NotificationForm,RegistrationForm
from datetime import datetime

# Create your views here.

def sales_line_chart_data(request):
    # Retrieve the sales data from the database
    products = Product.objects.all()
    sales_data = []
    labels = []

    # Calculate the sales data for each month
    for i in range(1, 13):
        month_sales = products.filter(created_at__month=i).aggregate(total_sales=models.Sum(models.F('price') * models.F('quantity')))['total_sales']
        sales_data.append(month_sales if month_sales else 0)
        labels.append(datetime(2000, i, 1).strftime('%b'))

    data = {
        'labels': labels,
        'data': sales_data
    }

    return JsonResponse(data)

def dashboard(request):
    return render(request, 'dashboard.html')


def product_sales_percentage(request):
    order = Order.objects.first()  # 假設你要使用第一個訂單的數據
    product_sales_percentage = order.get_product_sales_percentage()

    return render(request, 'dashboard.html', {'product_sales_percentage': product_sales_percentage})


def sales_percentage_pie_chart(request):
    orders = Order.objects.all()
    sales_data = []
    labels = []

    for order in orders:
        data = order.get_product_sales_percentage()
        sales_data.extend(data['data'])
        labels.extend(data['labels'])

    chart_data = {
        'labels': labels,
        'data': sales_data,
    }

    return render(request, 'sales_percentage_pie_chart.html', {'chart_data': chart_data})


def sales_trend_line_chart(request):
    orders = Order.objects.all()
    chart_data = {
        'labels': [],
        'data': [],
    }

    for order in orders:
        data = order.get_sales_trend_data()
        chart_data['labels'].extend(data['labels'])
        chart_data['data'].extend(data['data'])

    return render(request, 'sales_trend_line_chart.html', {'chart_data': chart_data})

def sales_chart_data(request):
    # 從 Product 模型中獲取銷售數據
    sales_data = Product.get_sales_chart_data()

    # 組織銷售數據為 labels 和 data
    labels = sales_data['labels']
    data = [sale * 100 for sale in sales_data['data']]  # 將銷售數據轉換為百分比

    # 構建回傳的 data 字典
    data = {
        "labels": labels,
        "data": data
    }
    
    return JsonResponse(data)

def stock_chart_data(request):
    # 實現產品庫存圖表數據的邏輯
    data = {
        "labels": ["Category 1", "Category 2", "Category 3"],
        "data": [10, 20, 30]
    }
    return JsonResponse(data)

def signup_view(request):
    User = get_user_model()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # 檢查使用者名稱是否已存在
            username = form.cleaned_data.get('username')
            User = get_user_model()
            if User.objects.filter(username=username).exists():
                messages.error(request, '該使用者名稱已被使用。請選擇其他使用者名稱。')
            else:
                form.save()
                messages.success(request, '註冊成功！')
                return redirect('home')
        else:
            messages.error(request, '註冊失敗。請檢查輸入內容。')
    else:
        form = RegistrationForm()
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

def shopping_view(request):
    products = ['Product 1', 'Product 2', 'Product 3']  # 假設這裡是您的產品數據
    return render(request, 'shopping.html', {'products': products})

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
def update_notification(request):
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
