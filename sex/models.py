from django.db import models

# Create your models here.
class Msex(models.Model):
    name = models.CharField(max_length=50, verbose_name="جنسیت")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "جنسیت ها"
        verbose_name = "جنسیت"