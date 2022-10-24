from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    premiere = models.DateField()
    classification = models.PositiveIntegerField()
    synopsis = models.TextField()

    genres = models.ManyToManyField(
        "genre.Genre",
        related_name="genres",
    )
