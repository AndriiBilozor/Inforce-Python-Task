from django.db import models
from employee.models import Employee
from menu.models import Menu


class Vote(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	voted_date = models.DateField(auto_now_add = True)

	def __str__(self):
		return f"Vote by {self.employee.last_name} for {self.menu.restaurant.name} on {self.voted_date}"
