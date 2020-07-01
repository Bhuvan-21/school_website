from django.db import models

# Create your models here.
class Student(models.Model):
    adm_no = models.IntegerField()
    first_name = models.TextField(max_length = 20)
    last_name = models.TextField(max_length = 20)
    subject = models.TextField(max_length = 20)
    working_days = models.IntegerField()
    present_days = models.IntegerField()
    half_days = models.IntegerField()
    absent_days = models.IntegerField()
