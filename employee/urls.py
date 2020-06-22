from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('device/', views.DeviceAPIView.as_view(), name="Device"),
  path('employee/', views.EmployeeAPIView.as_view(), name="Employee"),
  path('temperature/', views.TemperatureAPIView.as_view(), name="Temperature"),
  path('alltemp/', views.AllTemperatueAPIView.as_view(), name="All Temperature"),
  path('hightemp/', views.HighTemperatureAPIView.as_view(), name="High Temperature"),
]