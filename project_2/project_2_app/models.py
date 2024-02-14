from django.db import models


class Charger(models.Model):
    company_name = models.CharField(max_length=20)
    power_volt = models.IntegerField()
    charger_type = models.CharField(max_length=5)
    shop_name = models.CharField(max_length=10)
