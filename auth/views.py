from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from webapp.models import Profile, Visitor
    
class RegisterView(APIView):
    def get(self, request):
        return Response(template_name="register.html")
    
    def post(self, request):
        data = request.data
        user = User.objects.create_user(data['username'], data['email'], data['password'])
        user.save()
        return Response(template_name="login.html")

class AccountView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/auth/login')
        else:
            profile = Profile.objects.get(user=request.user)
            return Response({"profile": profile}, template_name="account.html")