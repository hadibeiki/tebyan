from django.contrib import admin

# Register your models here.
from registerEatekaf.models import Mregistereatekaf

class BookAdmin(admin.ModelAdmin):
    list_display = ('contact','mosque','payment',)
    list_filter = [
        "contact",
    ]
    search_fields = (
        "contact__melicode","contact__mobile",
    )

admin.site.register(Mregistereatekaf, BookAdmin)