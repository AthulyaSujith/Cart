from django.db import models
from cartapp.models import Product
# Create your models here.
class order(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
         db_table='order'
         ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.cart_id)

class cartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart= models.ForeignKey(order, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='cartItem'
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product
