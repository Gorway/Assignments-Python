import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from uuid import uuid4
from datetime import timedelta
from django.utils.timezone import now
import json

from django.contrib.auth import get_user_model

User = get_user_model()

import logging

logging.basicConfig(level=logging.DEBUG)

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def refresh_token(db):
    user = User.objects.create_user(username="testuser", password="testpassword")
    refresh = RefreshToken.for_user(user)
    return str(refresh)


@pytest.fixture
def authenticated_user(api_client, db):
    user = User.objects.create_user(username="testuser", password="testpassword")
    response = api_client.post(
        "login/",  # Replace with your login endpoint
        {"username": "testuser", "password": "testpassword"},
        format="json",
    )
    assert response.status_code == 200, f"Login failed: {response.data}"
    return {
        "user": user,
        "access_token": response.data.get("access"),
    }  # Ensure 'access' matches your API's response


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_data():
    return {"email": "testuser@examples.com", "password": "securepasswords"}


@pytest.fixture
def create_user(user_data):
    user = User.objects.create_user(
        username=user_data["email"],
        email=user_data["email"],
        password=user_data["password"],
    )
    return user


@pytest.mark.django_db
def test_refresh_token(api_client, refresh_token):
    response = api_client.post(
        "refresh/",  # Replace with your refresh endpoint
        {"refresh": refresh_token},  # Use the correct key expected by the backend
        format="json",
    )
    assert response.status_code == 200
    assert "access" in response.data


@pytest.mark.django_db
def test_user_registration(api_client, user_data):
    url = reverse("register")
    response = api_client.post(url, user_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert response.data["email"] == user_data["email"]


@pytest.mark.django_db
def test_user_login(api_client, create_user, user_data):
    url = reverse("login")
    response = api_client.post(url, user_data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.data
    assert "refresh_token" in response.data


@pytest.mark.django_db
def test_logout(api_client, refresh_token):
    response = api_client.post(
        "/api/logout/",  # Replace with your logout endpoint
        {"refresh_token": refresh_token},
        format="json",
    )
    assert response.status_code == 204


@pytest.mark.django_db
def test_retrieve_personal_info(api_client, create_user, user_data):
    url = reverse("me")
    login_url = reverse("login")
    login_response = api_client.post(login_url, user_data, format="json")
    access_token = login_response.data["access_token"]

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == user_data["email"]
    assert "id" in response.data


@pytest.mark.django_db
def test_update_personal_info(api_client, authenticated_user):
    token = authenticated_user["access_token"]
    response = api_client.put(
        "me/",
        {"username": "new_username"},
        HTTP_AUTHORIZATION=f"Bearer {token}",
        format="json",
    )
    assert response.status_code == 200
    assert response.data["username"] == "new_username"
