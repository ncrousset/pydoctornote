from django.db import models
from accounts.models import CustomUser as User
from django.urls import reverse


class Patient(models.Model):
    SEX = (
        ('m', 'masculine'),
        ('f', 'feminine'),
        ('o', 'other'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    insurance = models.CharField(max_length=20, blank=True, null=True)
    idd = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=15, choices=SEX)
    next_appointment = models.DateField(blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        """Returns the patient's full name"""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("detail_patient", kwargs={"pk": self.pk})
