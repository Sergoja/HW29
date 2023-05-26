from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from ads.models import Ad, Category, Selection
from users.models import User


class AdSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Ad


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class SelectionSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionListSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionDetailSerializer(ModelSerializer):
    items = AdSerializer(many=True)
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", required=False, read_only=True)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = '__all__'
