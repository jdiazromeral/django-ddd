from django.contrib import admin
from dummy_app.infrastructure.models import CustomModel


class CustomModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomModel, CustomModelAdmin)
