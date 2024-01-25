from django.contrib import admin

# Register your models here.
from ability.models import Mability

class BookAdmin(admin.ModelAdmin):

    search_fields = (
        "contact__melicode",
    )


admin.site.register(Mability, BookAdmin)