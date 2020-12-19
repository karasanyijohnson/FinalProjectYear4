from django.urls import path
from .views import MuseumListView, BookingListView, MuseumDetailView, CancelBookingView

app_name = 'museums'

urlpatterns = [
    path('', MuseumListView, name='MuseumListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('museum/<category>', MuseumDetailView.as_view(), name='MuseumDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView')
]
