from rest_framework_simplejwt.tokens import AccessToken
from django.utils.timezone import now, timedelta
from constance import config
from .models import RefreshToken


def create_refresh_token(user):
    expires_at = now() + timedelta(days=config.REFRESH_TOKEN_LIFETIME)
    refresh_token = RefreshToken.objects.create(user=user, expires_at=expires_at)
    return refresh_token.token


def create_access_token(user):
    token = AccessToken.for_user(user)
    token.set_exp(lifetime=timedelta(seconds=config.ACCESS_TOKEN_LIFETIME))
    return str(token)
