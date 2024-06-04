"""
FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
import Booking.views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    re_path(r'^$', Booking.views.index, name='index'),
    re_path(r'^home$', Booking.views.index, name='home'),
    path('cal/<int:year>/<int:month>/', Booking.views.Calendar, name='Calendar'),
    path('cal', Booking.views.Calendar, name='Calendar'),
    path('day/<int:year>/<int:month>/<int:day>', Booking.views.Day, name='day'),
    path('day', Booking.views.Day, name='day'),
    path('booking', Booking.views.Book, name='Booksiun'),
]