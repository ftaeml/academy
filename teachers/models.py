from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Ім’я")
    last_name = models.CharField(max_length=30, verbose_name="Призвіще")
    email = models.EmailField(verbose_name="електронна пошта")
    phone = models.CharField(max_length=25, verbose_name="телефон")
    date_of_birth = models.DateField(verbose_name="дата народження")
    user = models.ForeignKey(User,verbose_name="користувач")

    def __str__(self):
        return (self.last_name + " " + self.first_name)

    class Meta:
        verbose_name = "Вчитель"
        verbose_name_plural = "Вчителі"
        ordering = ['last_name']
