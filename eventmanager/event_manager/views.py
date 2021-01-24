from django.shortcuts import render
from . import templates
from .models import events_registered,participant_registrations
from django.utils import timezone
from .forms import event_hosting_form
from django.core.mail import send_mail
from django.contrib import messages
from django.db import IntegrityError
from datetime import date
import os
from twilio.rest import Client


def home(request):
    return render(request,"event_manager/home.html",{'title':"Home - Event Manager"})

def eventregisteration(request):
    form = event_hosting_form(request.POST or None)
    error_k=0
    try:
        if form.is_valid():
            D=form.cleaned_data
            print(D)
            email = D['host_email']
            for kk in events_registered.objects.all():
                if kk.host_email==email:
                    error_k=1
                    break
            if error_k==0:
                form.save()
                host_email = events_registered.objects.get(host_email=D['host_email'])
                msg='Hello User,\nYour event was registered on our portal.\nYour event ID : {host_email_id}\n Your Event Name:{host_email_name}\nPassword you created : {host_email_host_password}\nYou can see your event in active events tab and access your participation list.'.format(host_email_id=host_email.id,host_email_name=host_email.name,host_email_host_password=host_email.host_password)
                Subject = 'Your event is registered'
                To = [host_email.host_email]
                send_mail(Subject,msg,'eventmanagerportal@gmail.com',To,fail_silently=False)
                print('SEND MAIL action was taken for id',host_email.id)
                form=event_hosting_form()
        else:
            print(form.errors)
        context = {
            'form':form,
            'title':'Host Your Event',
            "k":error_k
        }
        return render(request,"event_manager/eventreg.html",context)
    except IntegrityError as e:
        return render(request,"event_manager/integrity.html")

def participantregisteration(request):
    error_email=0 #Participant Doesn't Exit
    error_reg=0 #Participant Exist, reg for another event
    if request.method=='POST':
        D=request.POST
        print(D)
        mainD={}
        for x,y in D.items():
            if x!="csrfmiddlewaretoken":
                mainD.update({x:y})
        print(f'\n{mainD}')
        email=mainD['participant_email']
        for m in participant_registrations.objects.all():
            if m.participant_email==email:
                error_email=1
                repeated=m
                break
            else:
                error_email=0
        if error_email==1:
            if repeated.eventId==mainD['eventId']:
                error_reg=1
            else:
                error_reg=0
        name_inst=events_registered.objects.filter(id=mainD['eventId']).first()
        if error_reg==0:
            participant_registrations.objects.create(**mainD)
            account_sid = "Your_SID_Token"
            auth_token = "Your_AUTH_Token"
            client = Client(account_sid, auth_token)
            to='+91'+mainD['participant_mobileno']
            message = client.messages.create(
                                body=f"You have been registered for event.\nDetails:\nID:{mainD['eventId']}\n{name_inst.name}\nFrom {name_inst.From} to {name_inst.To}\nLocation {name_inst.location}",
                                from_='Your_Number',
                                to=to
                            )

            print(message.sid)
        print(mainD)
        print('\nerror_email',error_email)
        print('\nerror_reg',error_reg)
        #print('\nerror_id',error_id)

    else:
        print(request.POST)
    context={
        'title':'Participate in Event',
        'reg':error_reg,
        'email':error_email,
        'events':events_registered.objects.filter(From__date__gte=date.today())
    }
    return render(request,"event_manager/participantreg.html",context)

def getlist(request):
    return render(request,"event_manager/getlist.html",{'title':"Your Event List"})

def get_eventslist(request):
    
    context = {
        'events':events_registered.objects.filter(From__date__gte=date.today()),
        "title":"Active Events Lists"
    }
    return render(request,"event_manager/eventslist.html",context)

def integrity(request):
    return render(request,"event_manager/integrity.html",{'title':'Error Occured'})