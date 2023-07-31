from django.shortcuts import render

from .models import *


def home(request):

    peoples = [
        {'name': 'Abhijeet Gupta', 'age': '26'},
        {'name': 'Rohan Sharma', 'age': '23'},
        {'name': 'Vicky Kaushal', 'age': '17'},
        {'name': 'Sandeep Roy', 'age': '36'}
    ]

    # for people in peoples:
    #     print(people)

    student = Student.objects.all()
    employees = Employees.objects.all()

    return render(request, "home/index.html", context={'page': 'home', 'peoples': peoples, 'student': student, 'employees': employees})
