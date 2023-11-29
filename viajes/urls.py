
from django.contrib import admin
from django.urls import path
from .views import ViajesIndexViews, ViajesFormViews, ViajesFlightsViews, ViajesAboutUsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ViajesIndexViews.as_view(), name = 'index'),
    path('index.html',ViajesIndexViews.as_view(), name = 'index'),
    path('form.html',ViajesFormViews.as_view(), name = 'form'),
    path('flights.html',ViajesFlightsViews.as_view(), name = 'flights'),
    path('about_us.html',ViajesAboutUsViews.as_view(), name = 'abouts_us')
]
