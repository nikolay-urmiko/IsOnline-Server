from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


from django.views import generic

#
class ChecksListView(generic.ListView):
    model = Checks
    context_object_name = 'dots_list'
    template_name = 'Check/list_urfaces.html'
    queryset = Checks.objects.all().prefetch_related('ur_facce')
   