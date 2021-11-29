from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=150)
    population = models.PositiveIntegerField()
    president = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}--{self.capital}'