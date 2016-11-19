from django.shortcuts import render
from .models import Student


def student(request):
    students = Student.objects.all()
    return render(request, "students/students.html", {"students": students})
