from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Trip

from django import forms

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class TripsBaseView(View):
    template_name = 'trip.html'
    model = Trip
    fields = '__all__'
    success_url = reverse_lazy('trip:all')


class TripsListView(TripsBaseView,ListView):    
    # THIS ALLOWS ME TO CREATE A VIEW WITH THE TRIPS
    # Paginate
    paginate_by = 3  # num pages
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip_list = self.get_queryset()
        
        paginator = Paginator(trip_list, self.paginate_by)
        page = self.request.GET.get('page')
        
        try:
            trips = paginator.page(page)
        except PageNotAnInteger:
            # If the page parameter is not a number, show the first page
            trips = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), show last page of results
            trips = paginator.page(paginator.num_pages)
        
        context['trip_list'] = trips
        return context
    

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
    
    # Change text field to date for date
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class TripDeleteView(TripsBaseView,DeleteView):
    template_name = "trip_delete.html"
    extra_context = {
        "type": "Delete trip"
    }

