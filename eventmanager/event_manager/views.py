from django.shortcuts import render
from . import templates
from .models import events_registered
from django.utils import timezone
from .forms import event_hosting_form,participant_registrations_form
from django.core.mail import send_mail


def home(request):
    return render(request,"event_manager/home.html",{'title':"Home - Event Manager"})

def eventregisteration(request):
    form = event_hosting_form(request.POST or None)
    if form.is_valid():
        D=form.cleaned_data
        print(D)
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
        'title':'Host Your Event'
    }
    return render(request,"event_manager/eventreg.html",context)

def participantregisteration(request):
    form=participant_registrations_form(request.POST or None)
    if form.is_valid():
        D=form.cleaned_data
        print(D)
        form=participant_registrations_form()
    context={
        'form':form,
        'title':'Participate in Event'
    }
    return render(request,"event_manager/participantreg.html",context)

def getlist(request):
    return render(request,"event_manager/getlist.html",{'title':"Your Event List"})

def get_eventslist(request):
    
    context = {
        'events':events_registered.objects.all(),
        "title":"Active Events Lists"
    }
    return render(request,"event_manager/eventslist.html",context)