from random import randint

from transliterate import translit
from django.utils.text import slugify


def generate_identifier() -> str:
    """
    Generating random identifier for exercises. Checks if it is unique
    :return: identifier
    """
    from .models import Exercise
    while True:
        identifier = randint(100000, 9999999)
        if str(identifier) not in [i.identifier for i in Exercise.objects.all()]:
            break
    return str(identifier)
