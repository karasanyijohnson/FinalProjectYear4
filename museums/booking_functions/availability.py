import datetime
from museums.models import Museum, Booking


def check_availability(museum, check_in, checkout_out):
    avail_list = []
    booking_list = Booking.objects.filter(museum=museum)
    for booking in booking_list:
        if booking.check_in > checkout_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
