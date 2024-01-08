from django.db import models


# Create your models here.
from django.utils import timezone


class Mcontact(models.Model):
    Marital={
        ("مجرد","مجرد"),
        ("متاهل","متاهل"),
    }
    name = models.CharField(max_length=200, verbose_name="نام")
    family = models.CharField(max_length=200, verbose_name="نام خانوادگی")
    dad = models.CharField(max_length=50, verbose_name="نام پدر")
    mobile = models.CharField(max_length=11, verbose_name="شماره موبایل")
    melicode = models.CharField(max_length=10, verbose_name="کد ملی")
    sex = models.ForeignKey("sex.Msex", verbose_name="جنسیت", on_delete=models.DO_NOTHING)
    age = models.IntegerField(verbose_name="سن")
    price = models.IntegerField(verbose_name="هزینه پرداختی", default=0)
    city = models.ForeignKey("city.Mcity", verbose_name="شهرستان", on_delete=models.DO_NOTHING)
    education = models.ForeignKey("education.Meducation", verbose_name="تحصیلات", on_delete=models.DO_NOTHING)
    marital = models.CharField(max_length=50, verbose_name="وضعیت تاهل", choices=Marital)
    otp = models.CharField(max_length=10, verbose_name="کد احراز هویت")
    otpcreatedtime = models.DateTimeField(verbose_name="زمان ایجاد کد احراز هویت", default=timezone.now)
    testimonial = models.BooleanField(verbose_name="رضایت نامه",)


    def __str__(self):
        return self.melicode

    class Meta:
        verbose_name_plural = "افراد"
        verbose_name = "فرد"