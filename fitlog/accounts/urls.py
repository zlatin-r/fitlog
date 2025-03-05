from django.urls import path

from fitlog.accounts.views import RegisterView, LogingView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LogingView.as_view(), name='login'),
]