
from django.contrib import admin
from django.urls import path, include
from .views import FlyIndexViews, FlyFormViews, FlyFlightsViews, FlyAboutUsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',FlyIndexViews.as_view(), name = 'index'),
    path('index/',FlyIndexViews.as_view(), name = 'index'),
    path('form/',FlyFormViews.as_view(), name = 'form'),
    path('flights/',FlyFlightsViews.as_view(), name = 'flights'),
    path('about_us/',FlyAboutUsViews.as_view(), name = 'abouts_us'),
    path("trips/", include("flyApp.urls")),
]
