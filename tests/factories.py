import factory
from ads.models import Ad, Category
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123qwe"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("ean", length=8)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    category = factory.SubFactory(CategoryFactory)
    description = "test text"
    price = 500
    author = factory.SubFactory(UserFactory)
    is_published = False
