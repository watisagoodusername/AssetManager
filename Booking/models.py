from __future__ import unicode_literals
from django.db import models
 
class Scheduling(models.Model):
    
    items = (
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
        ('mobile', 'Mobile'),
        ('camera', 'Camera'),
        )
    items = (
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
        ('mobile', 'Mobile'),
        ('camera', 'Camera'),
        )
    
    day = models.DateField(u'Day required')
    timebooked = models.TimeField(u'Time needed')
    returntime = models.TimeField(u'Return time')
    
    item = models.CharField(u'Item', max_length = 32, choices = items, default = 'Camera')
    
    person = models.CharField(u'User', max_length=32, default='USER')
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
        
    def __str__(self):
        return str(self.person) + ' booked ' + str(self.item) + ' from ' + str(self.timebooked) + ' to ' + str(self.returntime) + ' on ' + str(self.day)
    
