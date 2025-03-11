from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

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


class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'username': request.user.username,
        })

def login_page(request):
    return render(request, 'accounts/login.html')  # Render the login page

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





# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to homepage or dashboard
#         else:
#             return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
#
#     return render(request, 'accounts/login.html')
#
#
# def user_register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#
#         if password != password2:
#             return render(request, 'accounts/register.html', {'error': 'Passwords do not match'})
#
#         if User.objects.filter(username=username).exists():
#             return render(request, 'accounts/register.html', {'error': 'Username already exists'})
#
#         user = User.objects.create_user(username=username, email=email, password=password)
#         return redirect('login')  # Redirect to login page after successful registration
#
#     return render(request, 'accounts/register.html')
