import pytest
from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, admin_token):
    ad_list = AdFactory.create_batch(5)
    expected_response = {
        "id": 1,
        "owner": "admin",
        "name": "some selection",
        "items": [ad.pk for ad in ad_list]
    }

    data = {
        "name": "some selection",
        "items": [ad.pk for ad in ad_list]
    }
    response = client.post(
        f"/selection/",
        data=data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f"Bearer {admin_token}"
    )

    assert response.status_code == 201
    assert response.data == expected_response
