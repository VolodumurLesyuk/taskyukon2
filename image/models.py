from django.db import models


TYPES_IMAGE_CHOICES = (
    ("PNG", "png"),
    ("JPEG", "jpeg"),
)


class Image(models.Model):
    name = models.CharField(max_length=40, choices=TYPES_IMAGE_CHOICES, default="PNG")
    image = models.ImageField()
