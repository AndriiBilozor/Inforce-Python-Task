from django.db import models
from restaurant.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()

    def __str__(self):
        return f"Menu for {self.date} at {self.restaurant.name}"
