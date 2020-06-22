from django.contrib import admin
from .models import (
  Device,
  Temperature,
  Employee
)

# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
  pass

@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
  pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  pass