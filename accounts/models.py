from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class StudentData(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.student_id})"
    

class AdminData(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    admin_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.admin_id})"
