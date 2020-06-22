from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Employee(models.Model):
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  phone = PhoneNumberField(null=False, blank=False, unique=True)

  def __str__(self):
    return self.name


class Device(models.Model):
  name = models.CharField(max_length = 200)

  def __str__(self):
    return self.name


class Temperature(models.Model):
  temp_in_fahrenheit = models.FloatField(default=98.6)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  device = models.ForeignKey(Device, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)

  def __str__(self):
    return '%s : %s :%s' % (self.employee.name, self.device.name, self.temp_in_fahrenheit)
