from django import forms
from django.forms import ModelForm

from Booking.models import Scheduling

class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.TimeInput):
    input_type = 'time'

class SchedulingForm(ModelForm):
    class Meta:
        model = Scheduling
        fields = ('day', 'timebooked', 'returntime', 'item', 'person')
        widgets = {
            'day': DateInput(),
            'timebooked': TimeInput(),
            'returntime': TimeInput(),
        }