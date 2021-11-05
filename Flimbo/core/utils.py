from core.models import Image


def get_images(type_: str, id_):
    images = Image.objects.filter(entity_type=type_, entity_id=id_)
    return images
