from django.contrib import admin
from .models import events_registered,participant_registrations

admin.site.register(events_registered)
admin.site.register(participant_registrations)
