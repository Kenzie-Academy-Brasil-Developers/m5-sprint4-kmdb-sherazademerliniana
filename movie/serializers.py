from rest_framework import serializers

from genre.serializers import GenreSerializer

from movie.models import Movie
from genre.models import Genre


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id"]


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    premiere = serializers.DateField()
    duration = serializers.CharField(max_length=10)
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        genre_data = validated_data.pop("genres")

        movie_obj = Movie.objects.create(**validated_data)

        for genre_dict in genre_data:
            genre_obj, was_created = Genre.objects.get_or_create(**genre_dict)

            movie_obj.genres.add(genre_obj)

        return movie_obj

    def update(self, instance: Movie, validated_data: dict):
        genre_exists = validated_data.get("genres", "Key not found")

        if genre_exists != "Key not found":
            genre_data = validated_data.pop("genres")

            instance.genres.clear()

            for genre_dict in genre_data:
                genre_obj, was_created = Genre.objects.get_or_create(**genre_dict)
                instance.genres.add(genre_obj)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
