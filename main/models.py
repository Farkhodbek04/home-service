from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Services(models.Model):
    title = models.CharField(max_length = 255, default = 'Title')
    icon = models.ImageField()
    body = models.CharField(max_length = 255)

class Clients(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length = 25)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5, message='Rating must be less than or equal to 5.'),
            MinValueValidator(0, message='Rating must be greater than or equal to 0.')
        ]
    )
    opinion = models.CharField( max_length = 255)

class Contact(models.Model):
    name = models.CharField(max_length = 25)
    phone = models.CharField(max_length = 15)
    email = models.CharField(max_length = 30)
    

