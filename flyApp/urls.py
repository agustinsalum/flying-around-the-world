from django.contrib import admin
from django.urls import path , include


from .views import      TripListView   \
                    ,   TripDetailView \
                    ,   TripCreateView \
                    ,   TripUpdateView \
                    ,   TripDeleteView

app_name = "trip"

urlpatterns = [
    path("", TripListView.as_view(), name="all"),
    path("create/", TripCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", TripDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", TripUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TripDeleteView.as_view(), name="delete")

]