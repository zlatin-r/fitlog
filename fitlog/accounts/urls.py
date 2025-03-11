from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from fitlog.accounts.views import RegisterAPIView, LoginAPIView, LogoutApiView, login_page, UserDetailsView

urlpatterns = [
    path('api-register/', RegisterAPIView.as_view(), name='api-register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('login-page/', login_page, name='login-page'),  # Page to render the login form
    path('api-logout/', LogoutApiView.as_view(), name='api-logout'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('api/user-details/', UserDetailsView.as_view(), name='user-details'),
]
