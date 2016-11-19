from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Ім’я")
    last_name = models.CharField(max_length=30, verbose_name="Призвіще")
    email = models.EmailField(verbose_name="електронна пошта")
    phone = models.CharField(max_length=25, verbose_name="телефон")
    url = models.URLField(blank=True, verbose_name="посилання на сторінку в соцмережі")
    date_of_birth = models.DateField(verbose_name="дата народження")
    user = models.ForeignKey(User,verbose_name="користувач")
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Учень"
        verbose_name_plural = "Учні"
        ordering = ('last_name',)
