import pytest
from ads.serializer import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ad_list = AdFactory.create_batch(4)
    expected_response = {
        "count": 4,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ad_list, many=True).data
    }
    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == expected_response
