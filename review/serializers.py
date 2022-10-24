from rest_framework import serializers
from movie.serializers import MovieListSerializer, MovieSerializer
from review.exceptions import AlreadyExistsError

from user.serializers import UserListSerializer, UserSerializer

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    critic = UserListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"

    def validate_stars(self, value):
        if value > 10:
            raise serializers.ValidationError(
                detail="Ensure this value is less than or equal to 10."
            )
        elif value < 1:
            raise serializers.ValidationError(
                detail="Ensure this value is greater than or equal to 1."
            )

        return value

    def validate_review(self, value):
        review_already_exists = Review.objects.filter(review=value).exists()

        if review_already_exists:
            msg = "Review already exists."
            raise AlreadyExistsError(msg)

        return value
