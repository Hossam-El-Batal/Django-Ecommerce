from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True)
    
    def __str__(self)-> str:
        return f"{self.name} : {self.price}"
    class Meta:
        verbose_name = 'Mart Product'
        ordering = ['name'] 
        
# class Order(models.Model):
#     order_name = models.CharField(max_length=100)
#     transaction_order_id = models.ForeignKey('Transaction', on_delete=models.SET_NULL, null=True, related_name='orders')

#     def __str__(self) -> str:
#         return f"Order: {self.order_name} (Transaction ID: {self.transaction_order_id_id})"

# class Transaction(models.Model):
#     order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='transaction_detail')

#     def __str__(self) -> str:
#         return f"Transaction for Order ID: {self.order_id}"