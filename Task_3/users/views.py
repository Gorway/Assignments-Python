from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer, UserSerializer
from .utils import create_refresh_token, create_access_token
from .models import RefreshToken
from django.utils.timezone import now


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = get_user_model().objects.filter(email=email).first()

        if user and user.check_password(password):
            access_token = create_access_token(user)
            refresh_token = create_refresh_token(user)
            return Response(
                {"access_token": access_token, "refresh_token": str(refresh_token)},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        token_obj = RefreshToken.objects.filter(token=refresh_token).first()

        if token_obj and token_obj.expires_at > now():
            access_token = create_access_token(token_obj.user)
            new_refresh_token = create_refresh_token(token_obj.user)
            token_obj.delete()

            return Response(
                {"access_token": access_token, "refresh_token": str(new_refresh_token)},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": "Invalid or expired refresh token"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        token_obj = RefreshToken.objects.filter(token=refresh_token).first()

        if token_obj:
            token_obj.delete()
            return Response({"success": "User logged out."}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST
        )


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
