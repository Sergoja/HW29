# Generated by Django 4.2.1 on 2023-05-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
