from django.contrib import admin

# Register your models here.
from mosque.models import Mmosque


class BookAdmin(admin.ModelAdmin):
    list_display = ('name','id','velocity','sex',)

admin.site.register(Mmosque, BookAdmin)