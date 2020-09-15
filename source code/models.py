from django.db import models

# Create your models here.
class product_details(models.Model):
    product_id = models.IntegerField()
    product_img = models.ImageField(upload_to='product/')
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50 , default="")
    product_price = models.IntegerField()
    desc = models.CharField(max_length = 500)

    def __str__(self):
        return self.product_name
class user_details(models.Model):
    user_name = models.CharField(max_length = 50)
    psw = models.CharField(max_length = 100)
    age = models.IntegerField()
    xender = models.CharField(max_length = 10)
class user_cart(models.Model):
    user_name = models.CharField(max_length = 50)
    product_id = models.IntegerField()