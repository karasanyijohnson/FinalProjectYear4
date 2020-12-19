from django.urls import reverse

from museums.models import Museum


def get_museum_cat_url_list():
    """
        function that returns museum Category and Category URL list
    """
    museum = Museum.objects.all()[0]  # Getting a random "museum" object

    # Making a dictionary from "museum_CATEGORIES" Tuple on the "museum"
    museum_categories = dict(museum.MUSEUM_CATEGORIES)

    museum_cat_url_list = []  # Empty museum (Category.URL) List

    for category in museum_categories:  # for loop for populating the museum_cat_url_list
        museum_category = museum_categories.get(category)
        museum_url = reverse('museums:MuseumDetailView', kwargs={
            'category': category})

        museum_cat_url_list.append((museum_category, museum_url))
    return museum_cat_url_list
