from django.shortcuts import render
from django.http import HttpResponse
from .models import (
  Device,
  Temperature,
  Employee,
)
from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework.response import Response
from .serializers import (
  DeviceSerializer,
  EmployeeSerializer,
  # TemperatureSerializer,

)
# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")


class DeviceAPIView(APIView):
  def post(self, request, *args, **kwargs):
    if len(Device.objects.filter(name=request.data['name'])) > 0:
      return Response("Device already exists")
    serializer = DeviceSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
      device = serializer.save()
      data['response'] = "Device created"
      data['device_name']  = device.name
      return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeAPIView(APIView):
  def post(self, request, *args, **kwargs):
    if len(Employee.objects.filter(phone=request.data['phone'])) > 0:
      return Response("Employe with phone {} already exists".format(request.data['phone']))
    serializer = EmployeeSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
      employee = serializer.save()
      data['response'] = "Employee created"
      data["employee_name"] = employee.name
      return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TemperatureAPIView(APIView):
  def post(self, request, *args, **kwargs):
    data = dict()
    data['temp_in_fahrenheit'] = request.data['temperature']
    phone = Employee.objects.filter(phone=request.data['phone'])
    print("---------------",request.data)
    if len(phone)==0:
      return Response("No employee with given phone number exists, please create the employee first")
    elif len(phone) > 1:
      return Response("Multiple employee exist with this phone number")
    else:
      data['employee'] = phone[0]

    device = Device.objects.filter(name=request.data['device'])
    if len(device)==0:
      return Response("No such device Present")
    elif len(device) > 1:
      return Response("Multiple device present")
    else:
      data['device'] = device[0]
    try:
      temperature = Temperature.objects.create(**data)
      temperature.save()
    except:
      return Response("Sorry not able to register the temperature for the employee")

    degree_sign= u'\N{DEGREE SIGN}'
    response_data = dict()
    response_data['response'] = "Temperature registered for the employee"
    response_data['temperature'] = "{}{}F".format(temperature.temp_in_fahrenheit, degree_sign)
    return Response(response_data, status=status.HTTP_200_OK) 

class AllTemperatueAPIView(APIView):
  def get(self, request, *args, **kwargs):
    try:
      phone = Employee.objects.get(phone=request.data['phone'])
    except:
      return Response("Phone does not exist")
    queryset = Temperature.objects.filter(employee=phone, date__gte=request.data['startdate'], date__lte=request.data['enddate']).values('employee__name', 'temp_in_fahrenheit', 'device__name')
    return Response(queryset)

class HighTemperatureAPIView(APIView):
  def get(self, request, *args, **kwargs):
    queryset = Temperature.objects.filter(temp_in_fahrenheit__gt=100.0, date=request.data['date']).values('employee__name', 'employee__phone').distinct()
    return Response(queryset)  
    
