import datetime

import pytest


@pytest.fixture
@pytest.mark.django_db
def admin_token(client, django_user_model):
    username = "admin"
    password = "123qwe"
    birth_date = datetime.date(year=2000, month=5, day=5)
    email = "some@mail.com"

    django_user_model.objects.create(
        username=username,
        password=password,
        birth_date=birth_date,
        email=email,
        role="admin"
    )

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format='json'
    )
    access_token = response.data.get('access')
    return access_token


@pytest.fixture
@pytest.mark.django_db
def user_with_token(client, django_user_model):
    username = "admin"
    password = "123qwe"
    birth_date = datetime.date(year=2000, month=5, day=5)
    email = "some@mail.com"

    django_user_model.objects.create(
        username=username,
        password=password,
        birth_date=birth_date,
        email=email,
        role="admin"
    )

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format='json'
    )
    access_token = response.data.get('access')
    return access_token
