from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(null=True)
    street = models.CharField(null=True, max_length=100)
    house_number = models.CharField(null=True, max_length=10)
    town = models.CharField(null=True, max_length=100)
    city = models.CharField(null=True, max_length=100)
    news_notification = models.BooleanField(default=False)
    activity_notification = models.BooleanField(default=False)
    promotion_notification = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username


class Product(models.Model):
    # ...

    @classmethod
    def get_sales_chart_data(cls):
        # 獲取產品收入數據並處理成適合圖表的格式
        # ...

        return {
            'labels': chart_labels,
            'data': chart_data,
        }

    @classmethod
    def get_stock_chart_data(cls):
        # 獲取產品庫存數據並處理成適合圖表的格式
        # ...

        return {
            'labels': chart_labels,
            'data': chart_data,
        }

    # 添加其他圖表所需的模型方法或管理器方法