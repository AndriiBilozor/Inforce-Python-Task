from django.db import models


class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	address = models.CharField(max_length=255)

	def __str__(self):
		return self.name
