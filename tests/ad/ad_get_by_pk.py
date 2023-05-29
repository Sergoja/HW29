import factory
import pytest
from ads.serializer import AdListSerializer, AdDetailSerializer
from tests.factories import AdFactory, UserFactory, CategoryFactory


@pytest.mark.django_db
def test_ad_retrieve(client, admin_token):
    ad = AdFactory.create()
    response = client.get(
        f"/ad/{ad.pk}/",
        content_type='application/json',
        HTTP_AUTHORIZATION=f"Bearer {admin_token}"
    )

    assert response.status_code == 200
    assert response.data == AdDetailSerializer(ad).data
