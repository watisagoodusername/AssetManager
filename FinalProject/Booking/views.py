from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.
def index(request):
    return render(
        request,
        "Booking/index.html", 
        {
            'title': "Page of a website",
            'message': "Wahoo! It's a me, a website! ",
            'content': "Right now its "
        }
    )
def calender(request, year, month):
    month = month.title()
    mNum = list(calendar.month_name).index(month)
    mNum = int(mNum)

    layout = HTMLCalendar().formatmonth(year, mNum)

    return render(
        request,
        "Booking/displaytime.html",
        {
            'year': year,
            'month': month,
            'num': mNum,
            'calender': layout,
        }
        )