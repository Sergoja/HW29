from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def min_lenght(value):
    if len(value) < 5:
        raise ValidationError("Длина слова должна быть больше 5")


def check_name(value):
    if len(value) < 10:
        raise ValidationError("Длина слова должна быть больше 10")
