from django.db import models
from Stadium.models import Stadium
# Create your models here.

class Order(models.Model):
    STATUS_CHOISES=(
        (0,"epmty"),
        (1,"busy")
    )
    name=models.ForeignKey(Stadium,on_delete=models.CASCADE)
    begin_time=models.DateTimeField(default="")
    end_time=models.DateTimeField(default="")
    status=models.PositiveSmallIntegerField(choices=STATUS_CHOISES,default=0)

    class Meta:
        db_table='order'