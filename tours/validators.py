import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_country(value):
    """
    A function to validate the country field in the tours model
    """
    allowed_countries = ['england', 'ireland', 'scotland', 'wales']
    if value.lower() not in allowed_countries:
        raise ValidationError(_('Invalid country. Please enter one of the \
            following countries: England, Ireland, Scotland or Wales'))


def validate_img_extension(value):
    """
    A function to validate the image extension on image files for the tours
    model
    """
    ext = os.path.splitext(value.name)[1]
    valid_ext = ['.jpg', 'jpeg', '.png']
    if ext not in valid_ext:
        raise ValidationError(_("Invalid file extension. Supported file \
            extensions are .jpg, .jpeg & .png"))


def validate_image_size(value):
    """
    A function to validate the image size is not larger than 2MB when uploading
    an image to the tours model
    """
    max_size_mb = 2
    max_size_bytes = max_size_mb * 1024 * 1024

    if value.size > max_size_bytes:
        raise ValidationError(_("Invaild image size. Image size cannot be \
            larger than 2MB"))
