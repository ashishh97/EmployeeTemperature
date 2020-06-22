"# EmployeeTemperature" 

App made - employee

API's

1. For Device Registration (http://127.0.0.1:8000/app/device/) - POST
  Request : {
	"name":"Thermometer"
}
Response : {
    "response": "Device created",
    "device_name": "Cipla Thermometer"
}

2. For Employee Registration (http://127.0.0.1:8000/app/employee/) - POST
  Request : {
	"name" : "Deepak",
	"address" : "Kanpur",
	"phone" : "+919876512340"
}
Response : {
    "response": "Employee created",
    "employee_name": "Deepak"
}

3. For Temperature register for the employee with default as current date (http://127.0.0.1:8000/app/temperature/) - POST
  Request : {
	"temperature" : 100.3,
	"phone" : "+918769244665",
	"device" : "Cipla Thermometer"
}
  Response : {
    "response": "Temperature registered for the employee",
    "temperature": "100.3°F"
}

4. To get all temperature of an employee between the date (http://127.0.0.1:8000/app/alltemp/) - GET
  Request : {
	"phone" : "+918769244665",
	"startdate" : "2020-06-22",
	"enddate" : "2020-06-23"
}
  Response : [
    {
        "employee__name": "Ashish",
        "temp_in_fahrenheit": 101.2,
        "device__name": "Thermometer"
    },
    {
        "employee__name": "Ashish",
        "temp_in_fahrenheit": 101.2,
        "device__name": "Thermometer"
    },
    {
        "employee__name": "Ashish",
        "temp_in_fahrenheit": 99.5,
        "device__name": "Thermometer"
    },
    {
        "employee__name": "Ashish",
        "temp_in_fahrenheit": 100.3,
        "device__name": "Cipla Thermometer"
    }
]

5. To get all employee with temperature greter than 100°F for a particular date. (http://127.0.0.1:8000/app/hightemp/) - GET
  Request : {
	"date": "2020-06-22"
}
  Response : [
    {
        "employee__name": "Ashish",
        "employee__phone": "+918769244665"
    },
    {
        "employee__name": "Deepak",
        "employee__phone": "+919876512340"
    }
]
