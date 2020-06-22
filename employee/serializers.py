from .models import (
  Device,
  Temperature,
  Employee,
)

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)
from rest_framework import serializers



class DeviceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Device
    fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = "__all__"

# class TemperatureSerializer(serializers.ModelSerializer):
#   phone = CharField()
#   employee = CharField()
#   device = CharField()
#   class Meta:
#     model = Temperature
#     fields = ['temp_in_fahrenheit', 'employee', 'device', 'phone']

#   def create(self, validated_data):
#     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", validated_data)
#     phone = Employee.objects.filter(phone=validated_data['phone'])
#     validated_data.pop('phone')
#     validated_data['employee'] = phone[0].id
#     device = Device.objects.filter(name=validated_data['device'])
#     validated_data['device'] = device[0].id
#     temperature = Temperature.objects.create(**validated_data)
#     return temperature
