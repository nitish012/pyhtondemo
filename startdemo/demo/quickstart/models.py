from django.db import models
from quickstart.enums import Role
# Create your models here.

class Teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    role = models.CharField(max_length=10, null=False, blank=False, default=Role.NORMAL, choices=Role.CHOICES)
    

    def students(self):
        return self.student_set.all()

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(null=False, blank=False, default=0)
    roll_no = models.IntegerField(null=False, blank=False, default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
