from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('events/',events,name='events'),
    path('news/',news,name='news'),
    path('blogs/',blogs,name='blogs'),
    path('about/',about,name='about'),
    path('read/<int:pk>',read,name='read')
]