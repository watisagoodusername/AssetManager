from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from Booking.forms import SchedulingForm
from .models import Scheduling

# Create your views here.
def index(request):
    bookings = Scheduling.objects.all()
    return render(
        request,
        
        "Booking/index.html", 
        {
            'title': "Page of a website",
            'message': "Wahoo! It's a me, a website! ",
            'content': "Right now its ",
            'items':bookings
        }
    )
def Calendar(request, year = datetime.now().year, month = datetime.now().month):
    #month = month.title()
    #mNum = list(calendar.month_name).index(month)
    #mNum = int(mNum)

    layout = HTMLCalendar().formatmonth(year, month)

    return render(
        request,
        "Booking/displaytime.html",
        {
            'year': year,
            'month': month,
            'num': month,
            'calender': layout,
        }
        )

def Day(request, year = datetime.now().year, month = datetime.now().month, day=datetime.now().day):
    
    syear = str(year)
    smonth = str(month)
    if len(smonth) == 1:
        smonth = '0' + smonth
    sday = str(day)
    if len(sday) == 1:
        sday = '0' + sday

    date = syear + '-' + smonth + '-' + sday
    
    bookings =  Scheduling.objects.filter(day__contains=date)

    return render(
        request,
        "Booking/day.html",
        {
            'year': year,
            'month': month,
            'day': day,
            'bookings': bookings,
        }
        )

def Book(request):

    if request.method == "POST":
        form = SchedulingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('day')
    else:
        form = SchedulingForm()
        return render(request, 'Booking/new.html', {'form': form})
    