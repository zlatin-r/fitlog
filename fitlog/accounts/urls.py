from django.urls import path

from fitlog.accounts.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register')
]