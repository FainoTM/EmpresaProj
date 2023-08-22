from django.contrib import admin
from core.models import Cargo

@admin.register(Cargo)
class CargoAdimin(admin.ModelAdmin):
    pass