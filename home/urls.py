from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.real, name = 'about'),
    path('contant/', views.hay, name = 'contact'),

]
