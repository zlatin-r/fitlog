from django.urls import path

from fitlog.common.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]