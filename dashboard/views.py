from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    # 在這裡處理從後端獲取數據等相關邏輯
    context = {
        # 將需要傳遞到模板中的變數添加到context字典中
        'total_sales': 10000,
        'best_selling_product': 'Product A',
        # 其他變數...
    }
    return render(request, 'dashboard.html', context)