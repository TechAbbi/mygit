from django.db import models

# Create your models here.

from django.core.exceptions import ValidationError


def validate_number(value):
    if value > 5 or value < 0:  # Your conditions here
        raise ValidationError(f'{value} rating is out of range')


class MovieData(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField(validators=[validate_number])
    category = models.CharField(max_length=100, default="action")
