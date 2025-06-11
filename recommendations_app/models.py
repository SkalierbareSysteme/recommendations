import uuid

from django.db import models

# Create your models here.

class Recommendation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    posted_by = models.CharField(max_length=255)
    poster_id = models.CharField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    tags = models.JSONField()
    amount_of_recommendations = models.IntegerField()
    reviewer_id = models.CharField(max_length=255, blank=True)
    description = models.TextField()