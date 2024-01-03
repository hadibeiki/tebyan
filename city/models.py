from django.db import models


# Create your models here.
class Mcity(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام شهرستان")
    phone = models.CharField(max_length=11, verbose_name="شماره تلفن پشتیبانی")
    mobile = models.CharField(max_length=11, verbose_name="شماره موبایل پشتیبانی")
    user = models.CharField(max_length=200, verbose_name="نام کاربر پشتیبانی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "شهرستان ها"
        verbose_name = "شهرستان"