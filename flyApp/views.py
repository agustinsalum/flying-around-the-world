from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Trip

from django import forms

# Create your views here.


class TripsBaseView(View):
    template_name = 'trip.html'
    model = Trip
    fields = '__all__'
    success_url = reverse_lazy('trip:all')


class TripsListView(TripsBaseView,ListView):    
    # THIS ALLOWS ME TO CREATE A VIEW WITH THE TRIPS
    pass
    

class TripsDetailView(TripsBaseView,DetailView):
    template_name = "trip_detail.html"
    extra_context = {
        "type": "detail trip"
    }

class TripsCreateView(TripsBaseView,CreateView):
    template_name = "trip_create.html"
    extra_context = {
        "type": "Create trip"
    }
    
    # Change text field to date for date
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class TripUpdateView(TripsBaseView,UpdateView):
    template_name = "trip_create.html"
    extra_context = {
        "type": "Update Trip"
    }

class TripDeleteView(TripsBaseView,DeleteView):
    template_name = "trip_delete.html"
    extra_context = {
        "type": "Delete trip"
    }

