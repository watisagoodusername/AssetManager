from __future__ import unicode_literals
 
from django.contrib import admin
from .models import Scheduling
 
class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'timebooked', 'returntime', 'notes']