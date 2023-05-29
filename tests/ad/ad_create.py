import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):
    expected_response = {
        "id": 1,
        "is_published": False,
        "name": "some publication",
        "description": "",
        "price": 500,
        "image": None,
        "author": user.pk,
        "category": category.pk
    }

    data = {
        "is_published": False,
        "name": "some publication",
        "price": 500,
        "author": user.pk,
        "category": category.pk
    }
    response = client.post(
        "/ad/",
        data=data
    )

    assert response.status_code == 201
    assert response.data == expected_response
