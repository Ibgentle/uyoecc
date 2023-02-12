from django.db import models

# Create your models here.


class CommonInfo(models.Model):

    marital_choices = [('S', 'Single'), ('M', 'Married'),
            ('D', 'Divorced'), ('E', 'Engaged'), 
            ('C', 'Complicated')]
    gender_choices = [('F', 'Female'), ('M', 'Male')]

    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10,
            choices=gender_choices)
    marital_status = models.CharField(max_length=20,
            choices=marital_choices)
    residential_address = models.CharField(max_length=100,
            blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    nickname = models.CharField(max_length=50, 
            blank=True, null=True)
    hobbies = models.CharField(max_length=50,
            blank=True, null=True)
    favourite_food = models.CharField(max_length=100,
            blank=True, null=True)
    photo = models.ImageField(upload_to='staff/static/pictures', 
            blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['first_name']


class Agent(CommonInfo):
    grouping = [('Team A', 'A'), ('Team B', 'B')]
    team = models.CharField(max_length=10,
            choices=grouping)

class Management(CommonInfo):
    designation = models.CharField(max_length=50)

class Other(CommonInfo):
    department_choices = [('J', 'Janitors'), ('S', 'Security'),
            ('AP', 'Armed Personnel')]
    department = models.CharField(max_length=50,
            choices=department_choices)

