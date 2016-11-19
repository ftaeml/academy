from django.shortcuts import render
from .models import Teacher

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teachers.html", {"teachers": teachers})

# Create your views here.
