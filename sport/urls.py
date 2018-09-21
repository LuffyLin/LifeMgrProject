from django.urls import path
from . import views

app_name = 'sport'

urlpatterns = [

    path('', views.sportitem, name = 'sportitem'),
    path('record/<int:id>', views.sportrecord, name = 'sportrecord'),
]
