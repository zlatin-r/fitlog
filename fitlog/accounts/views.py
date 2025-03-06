import requests
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from fitlog.accounts.forms import LoginForm
from fitlog.accounts.serializers import UserSerializer, LoginRequestSerializer, LoginResponseSerializer, \
    LogoutRequestSerializer, LogoutResponseSerializer

UserModel = get_user_model()


class RegisterAPIView(CreateAPIView):
    queryset = UserModel
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@extend_schema(
    tags=['auth'],
    summary="Login endpoint",
    description="Authenticate a user and get back access and refresh tokens",
    request=LoginRequestSerializer,
    responses={
        200: LoginResponseSerializer,
        401: "Invalid username or password"
    }
)
@csrf_exempt
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({
                "error": "Invalid username or password",
            }, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Login successful",
        }, status=status.HTTP_200_OK)


@extend_schema(
    tags=['auth'],
    summary="Logout endpoint",
    description="Blacklist refresh token",
    request=LogoutRequestSerializer,
    responses={
        200: LogoutResponseSerializer,
        400: "Invalid or expired token",
    }
)
class LogoutApiView(APIView):
    # permission_classes = [IsAuthenticated] not needed
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                "message": "Logout successful",
            }, status=status.HTTP_200_OK)
        except TokenError:
            return Response({
                "error": "Invalid or expired token"
            }, status=status.HTTP_400_BAD_REQUEST)


API_URL_LOGIN = 'http://localhost:8000/auth/api-login/'


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login-page.html')

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            response = requests.post(API_URL_LOGIN, data={'username': username, 'password': password})

            if response.status_code == 200:
                tokens = response.json()
                access_token = tokens.get('access')
                refresh_token = tokens.get('refresh')

                # Store JWT tokens in session
                request.session['access_token'] = access_token
                request.session['refresh_token'] = refresh_token

                # Manually authenticate the user
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)

                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")

        return render(request, 'authentication/login-page.html', {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # Log the user out (clears the session)
        logout(request)
        # Redirect to the login page
        return redirect('home')  # Replace 'login' with the name of your login URL
