from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

UserModel = get_user_model()

class HomeView(TemplateView):
    def get_template_names(self):
        print(f"User authenticated: {self.request.user.is_authenticated}")
        if self.request.user.is_authenticated:
            return ['common/home-logged-in.html']
        return ['common/home-not-logged-in.html']
