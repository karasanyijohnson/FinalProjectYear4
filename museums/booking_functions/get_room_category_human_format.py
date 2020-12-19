from museums.models import Museum


def get_room_category_human_format(category):
    """
       A Function that takes computer format room_category and returns it in Human Format
    """
    room = Room.objects.all()[0]
    room_category = dict(room.MUSEUM_CATEGORIES).get(category, None)
    return room_category
