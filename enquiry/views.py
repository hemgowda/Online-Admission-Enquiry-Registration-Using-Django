from django.shortcuts import render
from enquiry.models import Admission,Student,Department
from django.http import HttpResponse,request

from django.views import generic


class StudentListView(generic.ListView):
    model = Student
    template_name = 'student_list.html'

class DepartmentListView(generic.ListView):
    model = Department
    template_name = 'department_list.html'
    