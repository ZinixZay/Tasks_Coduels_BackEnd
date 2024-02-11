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


def generate_slug(title: str, task_model) -> str:
    """
    Generating slug for new task
    :param title: task's title
    :param task_model: Task model
    :return: generated slug
    """
    slug = slugify(title, allow_unicode=True)
    slug = translit(slug, 'ru', reversed=True)
    slug = slug.replace("'", "")
    slug = slug.replace('"', '')
    similar_slugs = sorted([i.slug for i in task_model.objects.all() if slug in i.slug])
    match len(similar_slugs):
        case 0:
            return slug
        case 1:
            return slug + '1'
    slug = similar_slugs[-1]
    return slug[:len(slug) - 1] + (str(int(slug[-1]) + 1))
