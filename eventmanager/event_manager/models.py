from django.db import models

class events_registered(models.Model):
    host_email=models.EmailField(max_length=254)
    host_password=models.CharField(max_length=50,default='hostPass')
    host_mobileno=models.IntegerField(default='0000000000')
    name=models.CharField(max_length=50)
    description=models.TextField()
    location=models.CharField(max_length=140, default='NOT PROVIDED')
    From = models.DateTimeField()
    To = models.DateTimeField()
    deadline = models.DateTimeField()
    poster_link = models.TextField()

class participant_registrations(models.Model):
    event_id=models.IntegerField(default='0')
    participant_email=models.EmailField(max_length=254)
    participant_name=models.CharField(default='Not provided',max_length=254)
    participant_mobileno=models.IntegerField(default='0000000000')
    participant_type=models.CharField(default='Single',max_length=6)
    participant_total=models.IntegerField(default='1')
    