from django.contrib import admin
from taco.models import Taco
# Register your models here.

@admin.register(Taco)
class TacoAdmin(admin.ModelAdmin):
    pass