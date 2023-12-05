from django.contrib import admin
from django.urls import path , include
from .api.router import router

from .views import      TripsListView   \
                    ,   TripsDetailView \
                    ,   TripsCreateView \
                    ,   TripUpdateView \
                    ,   TripDeleteView

app_name = "trip"

urlpatterns = [
    path("", TripsListView.as_view(), name="all"),
    path("create/", TripsCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", TripsDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", TripUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TripDeleteView.as_view(), name="delete")

]

urlpatterns += router.urls