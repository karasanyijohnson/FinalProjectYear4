from museums.models import Museum


def get_museum_category_human_format(category):
    """
       A Function that takes computer format museum_category and returns it in Human Format
    """
    museum = Museum.objects.all()[0]
    museum_category = dict(museum.MUSEUM_CATEGORIES).get(category, None)
    return museum_category
