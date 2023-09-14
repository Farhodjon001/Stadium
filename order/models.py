from datetime import datetime

from django.db import models
from Stadium.models import Stadium
from customuser.models import CustomUser

time_choices = (
    (1, '8:00'),
    (2, '9:00'),
    (3, '10:00'),
    (4, '11:00'),
    (5, '12:00'),
    (6, '13:00'),
    (7, '14:00'),
    (8, '15:00'),
    (9, '16:00'),
    (10, '17:00'),
    (11, '18:00'),
    (12, '19:00'),
    (13, '20:00'),
)


# Create your models here.

class Order(models.Model):
    STATUS_CHOISES = (
        (0, "epmty"),
        (1, "busy")
    )
    time_choices = (
        (1, '8:00'),
        (2, '9:00'),
        (3, '10:00'),
        (4, '11:00'),
        (5, '12:00'),
        (6, '13:00'),
        (7, '14:00'),
        (8, '15:00'),
        (9, '16:00'),
        (10, '17:00'),
        (11, '18:00'),
        (12, '19:00'),
        (13, '20:00'),
    )
    name = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    begin_time = models.DateTimeField(choices=time_choices)
    end_time = models.DateTimeField(choices=time_choices)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOISES, default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'order'
        unique_together = (
            ('name', 'begin_time', 'end_time'),
        )
