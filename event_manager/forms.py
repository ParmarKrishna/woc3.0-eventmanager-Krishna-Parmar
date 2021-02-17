from django import forms
from .models import events_registered,participant_registrations
from django.core.exceptions import ValidationError
from django.forms.widgets import SplitDateTimeWidget


class event_hosting_form(forms.ModelForm):
    host_email=forms.EmailField(max_length=254,label='Your Email Address',widget=forms.TextInput(attrs={"placeholder":"Your Email Address"}))
    name=forms.CharField(max_length=50,label='Event Name',widget=forms.TextInput(attrs={"placeholder":"Your Event Name"}))
    description=forms.CharField(label='Event Description',widget=forms.Textarea(attrs={"placeholder":"Event Description","rows":1,"cols":20}))
    location=forms.CharField(max_length=140,label='Location of Event',widget=forms.TextInput(attrs={"placeholder":"Location of Event"}))
    From = forms.SplitDateTimeField(label='From date',input_date_formats=['%d/%m/%Y'],
                               input_time_formats=['%H:%M'], 
                               widget=SplitDateTimeWidget(date_format='%d/%m/%Y',
                                                          time_format='%H:%M',date_attrs={"placeholder":"DD/MM/YYYY"},time_attrs={"placeholder":"HH:MM"}))
    To = forms.SplitDateTimeField(label='To date',input_date_formats=['%d/%m/%Y'],
                               input_time_formats=['%H:%M'], 
                               widget=SplitDateTimeWidget(date_format='%d/%m/%Y',
                                                          time_format='%H:%M',date_attrs={"placeholder":"DD/MM/YYYY"},time_attrs={"placeholder":"HH:MM"}))
    deadline = forms.SplitDateTimeField(label='Your Event Registration Deadline',input_date_formats=['%d/%m/%Y'],
                               input_time_formats=['%H:%M'], 
                               widget=SplitDateTimeWidget(date_format='%d/%m/%Y',
                                                          time_format='%H:%M',date_attrs={"placeholder":"DD/MM/YYYY"},time_attrs={"placeholder":"HH:MM"}))
    poster_link = forms.CharField(required=False,label='Your Poster Link(if any)')
    host_password=forms.CharField(max_length=50,label='Create Your Host Password',widget=forms.PasswordInput(attrs={'placeholder':'Type in your password'}))
    host_mobileno=forms.IntegerField(label='Mobile Number')

    class Meta:
        model = events_registered
        fields = [
            'host_email','name','description','location','From','To','deadline','poster_link','host_password','host_mobileno'
        ]