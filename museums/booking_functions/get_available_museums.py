from museums.models import Museum
from .availability import check_availability


def get_available_museums(check_in, check_out):
    # Function that takes category and returns museum List

    museum_list = Museum.objects.filter(category=category)  # Get queryset of museums that satisfy the category
    # Init empty Museum list
    available_museums = []

    # Populate the list
    for museum in museum_list:
        if check_availability(museum, check_in, check_out):
            available_museums.append(museum)

    # Check for length of list
    if len(available_museums) > 0:
        return available_museums
    else:
        return None
