from django.urls import reverse

from museums.models import Museum


def get_room_cat_url_list():
    """
        function that returns Room Category and Category URL list
    """
    room = Museum.objects.all()  # [0]  Getting a random "Room" object

    # Making a dictionary from "ROOM_CATEGORIES" Tuple on the "Room"
    room_categories = dict(Museum.MUSEUM_CATEGORIES)

    room_cat_url_list = []  # Empty Room (Category.URL) List

    for category in room_categories:  # for loop for populating the room_cat_url_list
        room_category = room_categories.get(category)
        room_url = reverse('hotel:RoomDetailView', kwargs={
            'category': category})

        room_cat_url_list.append((room_category, room_url))
    return room_cat_url_list
