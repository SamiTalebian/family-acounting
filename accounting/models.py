from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

class PayRecord(models.Model):
    amount = models.PositiveBigIntegerField()
    payment_date_time =  jmodels.jDateField()
    description = models.TextField()
    created_user = models.ForeignKey(CustomUser,related_name="User_set",on_delete=models.CASCADE)
    request = models.ForeignKey('Request', related_name='Request_set',on_delete=models.DO_NOTHING)

class Request(models.Model):
    description = models.TextField()
    amount = models.PositiveBigIntegerField()
    payed = models.BooleanField(default=False)
    created_user = models.ForeignKey(CustomUser,related_name="User_in",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.description
