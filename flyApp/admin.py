from django.contrib import admin
from flyApp.models import Trip

# Register your models here.

@admin.register(Trip)
class TryAdmin(admin.ModelAdmin):
    pass