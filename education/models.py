from django.db import models

# Create your models here.
class Meducation(models.Model):
    name = models.CharField(max_length=50, verbose_name="سطح تحصیلات")


    class Meta:
        verbose_name_plural = "تحصیلات"
        verbose_name = "تحصیلات"


    def __str__(self):
        return self.name