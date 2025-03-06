from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from fitlog.accounts.views import RegisterAPIView, LoginAPIView, LogoutApiView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api-register'),
    path('login/', LoginAPIView.as_view(), name='api-login'),
    path('logout/', LogoutApiView.as_view(), name='api-logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]
