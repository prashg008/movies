import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Collections(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    movies = ArrayField(models.UUIDField(), default=list)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
    	unique_together = [['title', 'owner']]
