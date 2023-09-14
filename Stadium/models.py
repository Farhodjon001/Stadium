from django.db import models
from customuser.models import CustomUser
# Create your models here.

class Stadium(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    adress=models.URLField(default="")
    photo=models.ImageField(upload_to="stadium/",default="")
    contact=models.CharField(max_length=13)
    manager=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    class Meta:
        db_table='stadium'