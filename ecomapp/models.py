from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Apple_Product(models.Model):
    
    CAT=((1,'Iphones'),(2,'Ipad '),(3,'Apple Watch'),(4,'MacBook'),(5,'MacDesktop'),(6,'AppleTV'),(7,'AirBuds'),(8,'acceserise'))
    name=models.CharField(max_length=50,verbose_name='Product Name')
    cat=models.IntegerField(verbose_name='Category',choices=CAT)
    price=models.FloatField(verbose_name='Product Price')
 
    status=models.BooleanField(default=True,verbose_name='Available')


    pimage=models.ImageField(upload_to='image')

    # def __str__(self):
    #     return self.name
class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Apple_Product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model):
    order_id=models.IntegerField()
    pid=models.ForeignKey(Apple_Product,on_delete=models.CASCADE,db_column='pid')
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    qty=models.IntegerField()