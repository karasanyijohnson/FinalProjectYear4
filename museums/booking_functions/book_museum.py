from museums.models import Booking, Museum


def book_museum(request, museum, check_in, check_out):
    # Makes a Booking object and saves it
    booking = Booking.objects.create(
        user=request.user,
        museum=museum,
        check_in=check_in,
        check_out=check_out
    )
    booking.save()

    return booking
