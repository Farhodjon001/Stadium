from datetime import datetime

from django.db import models
from Stadium.models import Stadium
from customuser.models import CustomUser


# Create your models here.

class Order(models.Model):
    STATUS_CHOISES = (
        (0, "epmty"),
        (1, "busy")
    )
    name = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    begin_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOISES, default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'order'
