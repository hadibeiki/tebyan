from django.db import models

# Create your models here.

class MmosqueOpinion(models.Model):
    CHOIC = {
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    }
    peopleconvidienc = models.CharField(max_length=2, verbose_name='درصد راحتی مردم با سامانه',blank=True, null=True, choices=CHOIC)
    mosqueconvidient = models.CharField(max_length=2, verbose_name='درصد راحتی کار شما با سامانه', blank=True, null=True, choices=CHOIC)
    backupworker = models.CharField(max_length=2, verbose_name='تلاش پشتیبان سامانه در رفع امور مشکلات ', blank=True, null=True,choices=CHOIC)
    averagconnect = models.CharField(max_length=2, verbose_name='به طور متوسط چند بار با پشتیبانی تماس گرفتید', blank=True, null=True,choices=CHOIC)
    dataview = models.CharField(max_length=2, verbose_name='راحتی نمایش اطلاعات مسجد شما در بستر تبیان', blank=True, null=True,choices=CHOIC)
    youropinion = models.CharField(max_length=2, verbose_name='تا چه میزان سامانه تبیان را به دیگر مساجد معرفی می کنید', blank=True, null=True, choices=CHOIC)
    yourexprienc = models.CharField(max_length=2, verbose_name='با استفاده از تجربه خود از سال های دیگر به سامانه امتیاز دهید', blank=True, null=True, choices=CHOIC)
    backupaccess = models.CharField(max_length=2, verbose_name='در دسترس بودن پشتیبان', blank=True, null=True, choices=CHOIC)
    backupsolver = models.CharField(max_length=2, verbose_name='رفع مشکلات سامانه توسط پشتیبان', blank=True, null=True, choices=CHOIC)
    solver = models.CharField(max_length=2, verbose_name='تبیان تا چه حد مشکلات شما را برای ثبت نام اعتکاف حل کرده است', blank=True, null=True,choices=CHOIC)
    mosquechoices = models.CharField(max_length=2, verbose_name='میزان آسانی فرآیند انتخاب مسجد در سایت',blank=True, null=True,choices=CHOIC)
    paymethod = models.CharField(max_length=2, verbose_name='تا چه میزان روش پرداخت وجه اعتکاف به همین روش موجود در سایت مورد رضایت شماست', blank=True, null=True,choices=CHOIC)
    description = models.TextField(verbose_name="هر چی مخی بوگو:", blank=True, null=True,)


    def __str__(self):
        return self.id.__str__()

    class Meta:
        verbose_name_plural = "نظرسنجی مساجد"
        verbose_name = "نظرسنجی مسجد"