from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name="назва")
    description = models.CharField(max_length=100, verbose_name="опис")
    teacher = models.ForeignKey(Teacher)
    start = models.DateField(verbose_name="початок курсу")
    end = models.DateField(verbose_name="закінчення курсу")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
        ordering = ['-name']
