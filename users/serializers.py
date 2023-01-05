from django.forms import CharField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}, 'email': {
                    'validators': [
                        UniqueValidator(
                            queryset=User.objects.all()
                        ),
                    ],
                    "required": True
                }}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance