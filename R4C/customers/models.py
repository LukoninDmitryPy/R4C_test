from django.db import models


class Customer(models.Model):
    email = models.CharField(max_length=255,blank=False, null=False)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'