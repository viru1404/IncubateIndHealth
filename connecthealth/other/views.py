from django.shortcuts import render
from .models import patientlogin

from django.http import HttpResponse

def home(request):
	return HttpResponse("hii chotu other")


def createpatient(request):
	if request.method=='GET':
		#print("3")
		print(request.GET['name'])
		print(request.GET['email'])
		patientlogin.objects.create(name=request.GET['name'], email=request.GET['email'])
	return HttpResponse("login")
	
