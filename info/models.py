from django.db import models


class Student(models.Model):
    roll_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=200, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    standard = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.email