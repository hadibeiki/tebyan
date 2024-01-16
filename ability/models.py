from django.db import models

# Create your models here.
class Mability(models.Model):
    contact = models.ForeignKey("contact.Mcontact", verbose_name="فرد", on_delete=models.CASCADE)
    photo = models.BooleanField(verbose_name="عکاس",)
    editor = models.BooleanField(verbose_name="تدوین گر",)
    camera = models.BooleanField(verbose_name="فیلم بردار",)
    news = models.BooleanField(verbose_name="تولید خبر",)
    writer = models.BooleanField(verbose_name="نویسندگی",)
    adminis = models.BooleanField(verbose_name="مدیریت کانال مجازی",)
    poemer = models.BooleanField(verbose_name="شاعر",)
    madah = models.BooleanField(verbose_name="مداح و روضه خوانی",)
    adv = models.BooleanField(verbose_name="مبلغ",)
    backup = models.BooleanField(verbose_name="پشتیبانی",)
    engine = models.BooleanField(verbose_name="فنی و مهندسی",)
    teach = models.BooleanField(verbose_name="مدرس",)
    child = models.BooleanField(verbose_name="کودک و نوجوان",)

    def __str__(self):
        return self.contact.melicode

    class Meta:
        verbose_name_plural = "توانایی ها"
        verbose_name = "توانایی"