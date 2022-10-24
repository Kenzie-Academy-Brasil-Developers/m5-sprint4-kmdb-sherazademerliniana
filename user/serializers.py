from pyexpat import model
from rest_framework import serializers

from user.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(
        max_length=20,
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField()
    bio = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False,
    )
    is_critic = serializers.BooleanField(default=False)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    def validate_email(self, value):
        email_already_exists = User.objects.filter(email=value).exists()

        if email_already_exists:
            raise serializers.ValidationError(detail="email already exists")

        return value

    def validate_username(self, value):
        username_already_exists = User.objects.filter(username=value).exists()

        if username_already_exists:
            raise serializers.ValidationError(detail="username already exists")

        return value

    def create(self, validated_data):
        user_obj = User.objects.create_user(**validated_data)

        return user_obj
