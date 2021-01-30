from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('', views.home,name="Event-Manager-Home"),
    path('home', views.home,name="Event-Manager-Home"),
    path('eventregisteration',views.eventregisteration,name="Event-Manager-Register-Event"),
    path('participantregisteration',views.participantregisteration,name="Event-Manager-Participant"),
    path('getlist',views.getlist,name="Event-Manager-getlist"),
    path('get_eventslist',views.get_eventslist,name="Event-Manager-eventslist"),
    path('integrity',views.integrity,name="Integrity-Error")
]