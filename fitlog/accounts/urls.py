
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from fitlog.accounts import views
from fitlog.accounts.views import RegisterAPIView, LoginAPIView, LogoutApiView

urlpatterns = [
    path('api-register/', RegisterAPIView.as_view(), name='api-register'),
    path('api-login/', LoginAPIView.as_view(), name='api-login'),
    path('api-logout/', LogoutApiView.as_view(), name='api-logout'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('user-login/', views.user_login, name='login'),
    path('user-logout/', views.user_logout, name='logout'),
]
