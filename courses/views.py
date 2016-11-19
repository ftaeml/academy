from django.shortcuts import render
from .models import Course

def cours(request):
    courses = Course.objects.all()
    return render(request, "courses/courses.html", {"courses": courses})
