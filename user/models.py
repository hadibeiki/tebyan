from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, username, password=None, ):
        user = self.model(
            username=username,
            password=password,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, password=None,):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.is_verified = True
        user.save(using=self._db)
        return user

class Muser(AbstractBaseUser,PermissionsMixin):

    city = models.ForeignKey('city.Mcity', verbose_name="شهرستان", on_delete=models.CASCADE, null=True, blank=True)
    mosque = models.ForeignKey('mosque.Mmosque', verbose_name="نام مسجد", on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, verbose_name="نام کاربری", unique = True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    objects = MyAccountManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username.__str__()
