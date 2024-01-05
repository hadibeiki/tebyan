from django.db import models


# Create your models here.
class Mmosque(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام مسجد")
    address = models.TextField(verbose_name="آدرس")
    latitude = models.FloatField(verbose_name="عرض جغرافیایی")
    longtude = models.FloatField(verbose_name="طول جغرافیایی")
    price = models.IntegerField(verbose_name="هزینه اعتکاف")
    sex = models.ForeignKey("sex.Msex", verbose_name="جنسیت", on_delete=models.DO_NOTHING)
    velocity = models.IntegerField(verbose_name="ظرفیت")
    startage = models.IntegerField(verbose_name="سن شروع")
    endage = models.IntegerField(verbose_name="سن پایان")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    city = models.ForeignKey("city.Mcity", verbose_name="شهرستان",on_delete=models.DO_NOTHING,null=True)
    description = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "مساجد"
        verbose_name = "مسجد"