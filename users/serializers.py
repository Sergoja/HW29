from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from users.models import User, Location
from users.validators import DateValidator, RamblerValidation


class LocationSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Location


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(ModelSerializer):
    total_ads = IntegerField()

    class Meta:
        model = User
        exclude = ("password", )


class UserCreateUpdateSerializer(ModelSerializer):
    location = SlugRelatedField(
        required=False,
        many=True,
        slug_field="name",
        queryset=Location.objects.all()
    )
    birth_date = serializers.DateField(required=True, validators=[DateValidator()])
    age = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all()), RamblerValidation()])

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("locations", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        for loc_name in self._locations:
            loc, _ = Location.objects.get_or_create(name=loc_name)
            user.locations.add(loc)
        return user

    def save(self, **kwargs):
        user = super().save(**kwargs)
        if self._locations:
            user.locations.clear()
            for loc_name in self._locations:
                loc, _ = Location.objects.get_or_create(name=loc_name)
                user.locations.add(loc)
        return user

    class Meta:
        model = User
        fields = '__all__'
