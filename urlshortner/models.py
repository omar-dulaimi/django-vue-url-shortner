import uuid
from django.utils.http import int_to_base36
from django.db import models


def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)[:6]


class UserUrl(models.Model):
    originalUrl = models.CharField(max_length=2048)
    uniqueId = models.CharField(
        max_length=20, blank=True,  unique=True, default=id_gen, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.originalUrl
