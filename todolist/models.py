from django.db import models

class atasks(models.Model):
	task = models.CharField(max_length=255)
	pri = models.CharField(max_length=10)
	date = models.DateField(null=True)

	def __str__(self):
		return f"{self.id} {self.task} {self.pri} {self.date}"

class ftasks(models.Model):
	task = models.CharField(max_length=255)
	pri = models.CharField(max_length=10)
	date = models.DateField(null=True)

	def __str__(self):
		return f"{self.id} {self.task} {self.pri} {self.date}"