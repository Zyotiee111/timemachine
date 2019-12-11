from django.urls import path

from timeteller import views

urlpatterns = [
    path('', views.home, name='home'),
    path('today/',views.today, name = 'today'),
    path('timestamp/',views.timestamp, name = 'timestamp')
    
]