from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from fitlog.accounts.views import RegisterView, LogingView, LogoutApiView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LogingView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]