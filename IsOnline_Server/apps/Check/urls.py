from django.urls import path
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from .models import *

urlpatterns = [
    #path ('', views.index, name = 'index'),
    path('', views.ChecksListView.as_view(),  name='namedot'),
    #path('', views.UrFaceListView.as_view(),  name='urfacelist'),
    
    #url(r'^$', views.ChecksListView.as_view(),  name='namedot'),

    
	]
