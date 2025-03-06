from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View

UserModel = get_user_model()

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError

class HomeView(View):
    def get(self, request):
        access_token = request.session.get('access_token')
        if access_token:
            try:
                token = AccessToken(access_token)
                user_id = token['user_id']
                user = UserModel.objects.get(id=user_id)
                print("User is authenticated:", user.username)
            except TokenError:
                print("Invalid or expired token")
        else:
            print("No access token found")

        return render(request, 'common/home.html')
