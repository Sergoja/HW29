from ads.validators import min_lenght, check_name
from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(
        null=True,
        max_length=10,
        unique=True,
        validators=[min_lenght]
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200, validators=[check_name])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="ad_images", null=True, blank=True)
    is_published = models.BooleanField()

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
