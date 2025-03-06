from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from fitlog.accounts.views import RegisterAPIView, LoginAPIView, LogoutApiView, LoginView, LogoutView

urlpatterns = [
    path('api-register/', RegisterAPIView.as_view(), name='api-register'),
    path('api-login/', LoginAPIView.as_view(), name='api-login'),
    path('api-logout/', LogoutApiView.as_view(), name='api-logout'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
