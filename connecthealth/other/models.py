from django.db import models

class patientlogin(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	aadhar = models.CharField(max_length=200)
	address = models.CharField(max_length=200)

	def __str__(self):
		return self.name

