from rest_framework.fields import IntegerField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from users.models import User, Location


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

    def is_valid(self, *, raise_exception=False):
        self._skills = self.initial_data.pop("skills")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for skill in self._skills:
            skill_object, _ = User.objects.get_or_create(name=skill)
            user.skills.add(skill_object)

        user.save()
        return user
