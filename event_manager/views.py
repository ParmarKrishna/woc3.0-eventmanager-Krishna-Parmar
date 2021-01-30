from django.shortcuts import render,get_object_or_404
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
                account_sid = "Your Account SID"
                auth_token = "Your Auth token"
                client = Client(account_sid, auth_token)
                to='+91'+str(D['host_mobileno'])
                message = client.messages.create(
                                    body=f"Your Event has been registerd on Portal.\nEvent ID:{host_email.id}\nYour Password:{D['host_password']}\nYou can see your event in 'SEE ACTIVE EVENTS' tab and Access your participation list.\nThank your for registering.\n\n\n\nEvent Manager Portal",
                                    from_='YOUR NUMBER',
                                    to=to
                                )
                print('send message action was taken')
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
        email=mainD['participant_email']
        ID=mainD['eventId']
        print(ID)
        repeated=participant_registrations.objects.filter(participant_email=email)
        if repeated:
            error_email=1
            for repeats in repeated:
                if repeats.eventId==ID:
                    error_reg=1
                    break
                else:
                    error_reg=0
        else:
            error_email=0
        name_inst=events_registered.objects.get(id=mainD['eventId'])
        
        if error_reg==0:
            print('IOK')
            participant_registrations.objects.create(**mainD)
            account_sid = "Your Account SID"
            auth_token = "Your Auth token"
            client = Client(account_sid, auth_token)
            to='+91'+mainD['participant_mobileno']
            message = client.messages.create(
                                    body='Dear Participant,\nYour registration was successful.\nRegistration Details are provided below:\nYour Registered Name:{Name}\nYour Participant Type:{Type}\nTotal People:{People}\nEvent ID:{id}\n Your Event Name:{name}\nFrom {FromDate} to {ToDate}\nLocation {Location}\n\n\nEvent Manager Portal'.format(Name=mainD['participant_name'],Type=mainD['participant_type'],People=mainD['participant_total'],id=name_inst.id,name=name_inst.name,FromDate=name_inst.From,ToDate=name_inst.To,Location=name_inst.location),
                                    from_='Your NUmber',
                                    to=to
                                )

            #print(message.sid)
            msg='Dear Participant,\nYour registration was successful.\nRegistration Details are provided below:\nYour Registered Name:{Name}\nYour Participant Type:{Type}\nTotal People:{People}\nEvent ID:{id}\n Your Event Name:{name}\nFrom {FromDate} to {ToDate}\nLocation {Location}\n\n\nEvent Manager Portal'.format(Name=mainD['participant_name'],Type=mainD['participant_type'],People=mainD['participant_total'],id=name_inst.id,name=name_inst.name,FromDate=name_inst.From,ToDate=name_inst.To,Location=name_inst.location)
            Subject = 'Registration Successful.'
            To = [email]
            send_mail(Subject,msg,'eventmanagerportal@gmail.com',To,fail_silently=False)
            form=event_hosting_form()
        else:
            print(request.POST)
        print(mainD)
        print('\nerror_email',error_email)
        print('\nerror_reg',error_reg)
        #print('\nerror_id',error_id)

    else:
        print(request)
    context={
        'title':'Participate in Event',
        'reg':error_reg,
        'email':error_email,
        'events':events_registered.objects.filter(From__date__gte=date.today())
    }
    return render(request,"event_manager/participantreg.html",context)

def getlist(request):
    error_id=0
    error_pass=0
    if request.method=="POST":
        access_request=request.POST
        mainD={}
        for x,y in access_request.items():
            if x!="csrfmiddlewaretoken":
                mainD.update({x:y})
        event_ID=events_registered.objects.filter(id=mainD['access_event']).first()
        if event_ID:
            if event_ID.host_password==mainD['access_password']:
                print("200 OK")
                participants=participant_registrations.objects.filter(eventId=event_ID.id)
                con={
                    'title':'Your Participant List',
                    'participants':participants,
                    'id':event_ID
                    }
                return render(request,"event_manager/participantTable.html",con)
            else:
                error_pass=1
        else:
            error_id=1
        print(error_id)
        print(error_pass)

    else:
        print(request)
    context={
        'pass':error_pass,
        'id':error_id,
        'title':"Your Event List"}
    return render(request,"event_manager/getlist.html",context)

def get_eventslist(request):
    context = {
        'events':events_registered.objects.filter(From__date__gte=date.today()),
        "title":"Active Events Lists"
    }
    return render(request,"event_manager/eventslist.html",context)

def integrity(request):
    return render(request,"event_manager/integrity.html",{'title':'Error Occured'})
    
