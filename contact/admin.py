from django.contrib import admin

# Register your models here.
from contact.models import Mcontact

class BookAdmin(admin.ModelAdmin):
    list_display = ('melicode','name','mobile',)
    list_filter = [
        "melicode",
    ]
    search_fields = (
        "melicode",'name','family','mobile',
    )
admin.site.register(Mcontact, BookAdmin)
