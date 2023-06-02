import pytest
from users.models import *  
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_get_account(api_client, account):
    response = api_client.get(reverse('account-detail'))

    assert response.status_code == status.HTTP_200_OK

    account_data = dict(response.data) 
    assert account_data['username'] == account.username
    assert account_data['email'] == account.email


@pytest.mark.django_db
def test_update_account_put(api_client, account):

    payload = {
        "username": "test",
        "email": "test@gmail.com",
        "first_name": "Imie",
        "last_name": "Nazwisko",
        "born_date": "2023-05-03"
    }

    response = api_client.put(f'/api/account/', payload, format='json')

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_account_patch(api_client, account):

    payload = {
        "first_name": "Imie",
        "last_name": "Nazwisko"
    }

    response = api_client.patch(f'/api/account/', payload, format='json')

    assert response.status_code == 200