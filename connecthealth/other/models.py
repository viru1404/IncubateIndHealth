from django.db import models

class userlogin(models.Model):
	usertype = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	aadhar = models.CharField(max_length=200)

	def __str__(self):
		return self.name

