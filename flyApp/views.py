from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Trip

# Create your views here.


class TripBaseView(View):
    template_name = 'trip.html'
    model = Trip
    fields = '__all__'
    success_url = reverse_lazy('trip:all')


class VinosListView(TripBaseView,ListView):
    
    # THIS ALLOWS ME TO CREATE A VIEW WITH THE TRIPS
    pass
    

class TripDetailView(TripBaseView,DetailView):
    template_name = "vino_detail.html"

class TripCreateView(TripBaseView,CreateView):
    template_name = "trip_create.html"
    extra_context = {
        "type": "Create trip"
    }


class TripUpdateView(TripBaseView,UpdateView):
    template_name = "trip_create.html"
    extra_context = {
        "type": "Update Trip"
    }

class TripDeleteView(TripBaseView,DeleteView):
    template_name = "trip_delete.html"
    extra_context = {
        "type": "Delete trip"
    }

