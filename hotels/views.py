from django.shortcuts import render, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, View, DeleteView
from .models import Room, Booking
from .forms import AvailabilityForm
from hotel.booking_functions.get_room_cat_url_list import get_room_cat_url_list
from hotel.booking_functions.get_room_category_human_format import get_room_category_human_format
from hotel.booking_functions.get_available_rooms import get_available_rooms
from hotel.booking_functions.book_room import book_room


# Create your views here.
def RoomListView(request):
    room_category_url_list = get_room_cat_url_list()
    context = {
        "room_list": room_category_url_list,
    }
    return render(request, 'room_list_view.html', context)


class BookingListView(ListView):
    model = Booking
    template_name = "booking_list_view.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class RoomDetailView(View):
    # Generic "View" based RoomDetailView
    def get(self, request, *args, **kwargs):

        # Get Room Category from kwargs
        category = self.kwargs.get('category', None)

        # Get the Human readable format
        human_format_room_category = get_room_category_human_format(category)

        # Initialize empty form
        form = AvailabilityForm()

        # Check for invalid category names
        if human_format_room_category is not None:
            context = {
                'room_category': human_format_room_category,
                'form': form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist!')

    def post(self, request, *args, **kwargs):

        # Get Room Category from kwargs
        category = self.kwargs.get('category', None)

        # Pass Request.Post into AvailabilityForm
        form = AvailabilityForm(request.POST)

        # Checking form validity
        if form.is_valid():
            data = form.cleaned_data

        # Get Available Rooms
        available_rooms = get_available_rooms(category, data['check_in'], data['check_out'])

        if available_rooms is not None:
            booking = book_room(request, available_rooms[0], data['check_in'], data['check_out'])
            return HttpResponse(booking)
        else:
            return HttpResponse("All of this category of rooms are booked!! try another one")


class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('hotel:BookingListView')
