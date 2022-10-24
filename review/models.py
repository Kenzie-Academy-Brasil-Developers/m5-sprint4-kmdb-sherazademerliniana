from django.db import models

# Create your models here.


class RecomendationChoice(models.TextChoices):
    MUST_WATCH = "Must Watch"
    SHOULD_WATCH = "Should Watch"
    AVOID_WATCH = "Avoid Watch"
    DEFAULT = "No Opinion"


class Review(models.Model):
    stars = models.PositiveIntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(
        max_length=50,
        choices=RecomendationChoice.choices,
        default=RecomendationChoice.DEFAULT,
    )

    movie = models.ForeignKey(
        "movie.Movie",
        on_delete=models.CASCADE,
        related_name="movie_reviews",
    )

    critic = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="user_reviews",
    )
