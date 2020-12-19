from django.shortcuts import render, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, View, DeleteView
from .models import Museum, Booking
from .forms import AvailabilityForm
from museums.booking_functions.get_museum_cat_url_list import get_museum_cat_url_list
from museums.booking_functions.get_museum_category_human_format import get_museum_category_human_format
from museums.booking_functions.get_available_museums import get_available_museums
from museums.booking_functions.book_museum import book_museum


# Create your views here.
def MuseumListView(request):
    museum_category_url_list = get_museum_cat_url_list()
    context = {
        "museum_list": museum_category_url_list,
    }
    return render(request, 'museum_list_view.html', context)


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


class MuseumDetailView(View):
    # Generic "View" based MuseumDetailView
    def get(self, request, *args, **kwargs):

        # Get Museum Category from kwargs
        category = self.kwargs.get('category', None)

        # Get the Human readable format
        human_format_museum_category = get_museum_category_human_format(category)

        # Initialize empty form
        form = AvailabilityForm()

        # Check for invalid category names
        if human_format_museum_category is not None:
            context = {
                'museum_category': human_format_museum_category,
                'form': form,
            }
            return render(request, 'museum_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist!')

    def post(self, request, *args, **kwargs):

        # Get Museum Category from kwargs
        category = self.kwargs.get('category', None)

        # Pass Request.Post into AvailabilityForm
        form = AvailabilityForm(request.POST)

        # Checking form validity
        if form.is_valid():
            data = form.cleaned_data

        # Get Available Museums
        available_museums = get_available_museums(category, data['check_in'], data['check_out'])

        if available_museums is not None:
            booking = book_museum(request, available_museums[0], data['check_in'], data['check_out'])
            return HttpResponse(booking)
        else:
            return HttpResponse("All of this category of museums are booked!! try another one")


class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('museums:BookingListView')
