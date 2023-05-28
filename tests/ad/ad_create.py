import pytest
from ads.serializer import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_create(client):
    expected_response = {
        "id": 1,
        "is_published": False,
        "name": "some publication",
        "description": "",
        "price": 500,
        "image": None,
        "author": 1,
        "category": 1
    }

    data = {
        "is_published": False,
        "name": "some publication",
        "price": 500,
        "author": 1,
        "category": 1
    }
    response = client.post(
        "/ad/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response
