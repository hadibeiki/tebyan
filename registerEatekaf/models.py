from django.db import models

# Create your models here.
class Mregistereatekaf(models.Model):
    pyorno={
        ("خیر","خیر"),
        ("بله","بله"),
    }
    contact = models.ForeignKey("contact.Mcontact", verbose_name="فرد", on_delete=models.CASCADE)
    mosque = models.ForeignKey("mosque.Mmosque", verbose_name="مسجد", on_delete=models.CASCADE)
    payment = models.CharField(max_length=50, verbose_name="وضعیت پرداخت", choices=pyorno, blank=True, null=True)


    def __str__(self):
        return self.mosque.name

    class Meta:
        verbose_name_plural = "ثبت نام های اعتکاف"
        verbose_name = "ثبت نام"