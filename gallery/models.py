from django.db import models

# Create your models here.
class Mgallery(models.Model):
    mosqe = models.ForeignKey("mosque.Mmosque", verbose_name="مسجد", on_delete=models.CASCADE)
    mFile = models.FileField(verbose_name="فایل", upload_to="media")


    def __str__(self):
        return self.mosqe.name


    class Meta:
        verbose_name_plural = "گالری ها"
        verbose_name = "گالری"