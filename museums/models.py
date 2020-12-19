from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

# Create your models here.
from django.urls import reverse_lazy


class Museum(models.Model):

    MUSEUM_CATEGORIES = (

        ("CAMPAIGN AGAINST GENOCIDE", "CAMPAIGN AGAINST GENOCIDE"),
        ("RWANDA ART", "RWANDA ART"),
        ("KING'S PALACE", "KING'S PALACE"),
        ("NATIONAL LIBERATION", "NATIONAL LIBERATION"),
        ("ENVIRONMENT", "ENVIRONMENT"),
        ("KWIGIRA", "KWIGIRA"),
        ("KANDT'S HOUSE", "KANDT'S HOUSE"),
        ("ETHNOGRAPHIC", "ETHNOGRAPHIC")

    )
    category = models.CharField(max_length=50, choices=MUSEUM_CATEGORIES)
    title  =  models.CharField(max_length=200)
    description = models.TextField()
    image  =  models.ImageField(upload_to='media/museums')
    location  = models.CharField(max_length=200)


    def __str__(self):
        return f'{dict(self.MUSEUM_CATEGORIES)[self.category]}'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    # def __str__(self):
    #     return f'from={self.check_in.strftime("%d-%b-%Y %H:%M")} To={self.check_out.strftime("%d-%b-%Y %H:%M")}'

    def get_museum_category(self):
        museum_categories = dict(self.museum.MUSEUM_CATEGORIES)
        museum_category = museum_categories.get(self.museum.category)
        return museum_category

    def get_cancel_booking_url(self):
        return reverse_lazy('museums:CancelBookingView', args=[self.pk, ])
