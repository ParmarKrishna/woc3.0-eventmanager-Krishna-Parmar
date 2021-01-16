from django import forms
from .models import events_registered,participant_registrations


class event_hosting_form(forms.ModelForm):
    host_email=forms.EmailField(max_length=254,label='Your Email Address',widget=forms.TextInput(attrs={"placeholder":"Your Email Address"}))
    name=forms.CharField(max_length=50,label='Event Name',widget=forms.TextInput(attrs={"placeholder":"Your Event Name"}))
    description=forms.CharField(label='Event Description',widget=forms.Textarea(attrs={"placeholder":"Event Description","rows":1,"cols":20}))
    location=forms.CharField(max_length=140,label='Location of Event',widget=forms.TextInput(attrs={"placeholder":"Location of Event"}))
    From = forms.DateTimeField(label='From date')
    To = forms.DateTimeField(label='To date')
    deadline = forms.DateTimeField(label='Your Event Registration Deadline')
    poster_link = forms.CharField(required=False,label='Your Poster Link(if any)')
    host_password=forms.CharField(max_length=50,label='Create Your Host Password',widget=forms.PasswordInput(attrs={'placeholder':'Type in your password'}))
    host_mobileno=forms.IntegerField(label='Mobile Number')

    class Meta:
        model = events_registered
        fields = [
            'host_email','name','description','location','From','To','deadline','poster_link','host_password','host_mobileno'
        ]

class participant_registrations_form(forms.ModelForm):
    choices=(('Single','Single'),
    ('Group','Group'))
    event_id=forms.IntegerField(label='Event ID')
    participant_email=forms.EmailField(max_length=254,label='Email Address')
    participant_name=forms.CharField(max_length=254,label='Name')
    participant_mobileno=forms.IntegerField(label='Mobile Number')
    participant_type=forms.CharField(label='Type of Participation',widget=forms.RadioSelect(choices=choices))
    participant_total=forms.IntegerField(label='Total Group Member',widget=forms.NumberInput(attrs={'class':'reveal-if-group'}))
    class Meta:
        model = participant_registrations
        fields = [
            'event_id','participant_email','participant_name','participant_mobileno','participant_type','participant_total'
        ]