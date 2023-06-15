"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic.base import TemplateView
from dashboard.views import dashboard_view, signup_view,settings_view, update_profile, update_notifications
from dashboard import views
from django.views.generic.shopping import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', dashboard_view, name='home'),
    path('signup/', signup_view ,name="signup"),
    path('dashboard/', dashboard_view, name="dashboard"),
    path('settings/', settings_view, name="settings"),
    path('update_profile/', update_profile, name="update_profile"),
    path('update_notifications/', update_notifications, name="update_notifications"),
    path('sales-chart-data/', views.sales_chart_data, name='sales_chart_data'),
    path('stock-chart-data/', views.stock_chart_data, name='stock_chart_data'),
    path('sales-line-chart-data/', views.sales_line_chart_data, name='sales_line_chart_data'),
    path('shopping/', views.shopping_page, name='shopping'),
    path('customer/', views.customer_view, name='customer'),
]
