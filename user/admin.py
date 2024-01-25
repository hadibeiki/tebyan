from django.contrib import admin
from user.models import Muser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','username','mosque','city',)


admin.site.register(Muser,BookAdmin)