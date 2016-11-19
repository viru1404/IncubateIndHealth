from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.home, name="OtherHome"),
	url(r'^register/patient/$',views.createpatient, name="RegisterPatient")

]