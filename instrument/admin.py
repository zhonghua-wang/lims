from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass