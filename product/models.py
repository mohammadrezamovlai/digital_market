from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey(to=Product,related_name='product_file',on_delete=models.CASCADE)
    file = models.FileField(upload_to='product/%y/%m/%d')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'


class Category(models.Model):
    product = models.ManyToManyField(to=Product,related_name='product_category')
    title = models.CharField(max_length=40)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Cart(models.Model):
    user = models.ForeignKey(to=User,related_name='user_carts',on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f'{self.user.username}'
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())
    
    @property
    def total_items(self):
        return self.items.count()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items',verbose_name='سبد خرید')
    product = models.ForeignKey('Product', on_delete=models.CASCADE,related_name='cart_items',verbose_name='محصول')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    price = models.IntegerField(verbose_name='قیمت هنگام اضافه شدن')  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ اضافه شدن')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        unique_together = ('cart', 'product')  
    
    def __str__(self):
        return f"{self.product.title} - {self.quantity}"
    


