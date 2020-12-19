from hotel.models import Room
from .availability import check_availability


def get_available_rooms(category, check_in, check_out):
    # Function that takes category and returns Room List

    room_list = Room.objects.filter(category=category)  # Get queryset of rooms that satisfy the category

    # Init empty form list
    available_rooms = []

    # Populate the list
    for room in room_list:
        if check_availability(room, check_in, check_out):
            available_rooms.append(room)

    # Check for length of list
    if len(available_rooms) > 0:
        return available_rooms
    else:
        return None
