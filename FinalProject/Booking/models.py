from __future__ import unicode_literals
from django.db import models
 
class Scheduling(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    timebooked = models.TimeField(u'Time needed', help_text=u'Time needed')
    returntime = models.TimeField(u'Return time', help_text=u'Return time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'