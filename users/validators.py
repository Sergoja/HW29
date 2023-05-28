import datetime

from rest_framework import serializers


class DateValidator:
    def __call__(self, value):
        today = datetime.date.today()
        age = today.year - value.year - 1 + ((today.month, today.day) >= (value.month, value.day))
        if age < 9:
            raise serializers.ValidationError('Регистрация возможна с 9 лет')
