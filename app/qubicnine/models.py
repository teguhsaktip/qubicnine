import uuid

from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    """
        Base model for every model
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='%(class)s_created_by',
        on_delete=models.CASCADE,
        db_column='created_by',
        null=True,
        blank=True
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='%(class)s_modified_by',
        on_delete=models.CASCADE,
        db_column='modified_by',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
