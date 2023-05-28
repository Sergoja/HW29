import pytest
from ads.serializer import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_retrieve(client, ad, admin_token):
    expected_response = {
        "id": ad.pk,
        "is_published": False,
        "name": "some publication",
        "description": "",
        "price": 500,
        "image": None,
        "author": ad.author_id,
        "category": ad.category_id
    }
    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION=f"Token {admin_token}"
    )

    assert response.status_code == 200
    assert response.data == expected_response
