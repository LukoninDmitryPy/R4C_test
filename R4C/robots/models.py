from django.db import models


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    class Meta:
        verbose_name = 'Робот'
        verbose_name_plural = 'Роботы'

    def __str__(self):
        return f'{self.model}-{self.version}'
