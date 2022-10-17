from django.db import models

from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    slug = AutoSlugField(populate_from='full_name', blank=True, null=True)
    full_name = models.CharField(max_length=150, null=True)
    position = models.CharField(max_length=100, null=True)
    employment_date = models.DateField(null=True)
    salary = models.PositiveIntegerField(null=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    class MPTTMeta:
        order_insertion_by = ["full_name"]

    def __str__(self) -> str:
        return self.full_name
