from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from fitlog.accounts.views import RegisterAPIView, LoginAPIView, LogoutApiView

urlpatterns = [
    path('api-register/', RegisterAPIView.as_view(), name='api-register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('api-logout/', LogoutApiView.as_view(), name='api-logout'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]
