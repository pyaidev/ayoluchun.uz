from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField("Yaratilgan vaqti", auto_now_add=True)
    updated_at = models.DateTimeField("O`zgartirilgan vaqti", auto_now=True)

    class Meta:
        abstract = True