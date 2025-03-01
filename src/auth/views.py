from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from webapp.models import Profile
from rest_framework import response
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model, authenticate, logout, login
from webservice.settings import ADMIN_USER_EMAIL


# TODO: FIX registering
class RegisterView(APIView):
    def get(self, request):
        form = User()
        serializer = UserRegisterSerializer(form)
        return response.Response(
            {"serializer": serializer}, template_name="register.html"
        )

    def post(self, request: Request):
        # Serialize the request data
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                serializer.validated_data["username"],
                serializer.validated_data["email"],
                serializer.validated_data["password"],
                is_active=False,
            )
            # Send verification email
            token = account_activation_token.make_token(user)
            verification_url = (
                request.build_absolute_uri(reverse("auth:verify")) + f"?token={token}"
            )
            send_mail(
                subject="Verify your account",
                message=f"Please click on the link to verify your account: {verification_url}",
                from_email=ADMIN_USER_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            user.save()
            return redirect("/auth/check-email/")
        else:
            # If the data is not valid, return the form with errors
            return Response(
                {"serializer": serializer}, template_name="register.html", status=400
            )


@api_view(["GET"])
def check_email(request):
    return Response(template_name="check_email.html")


def get_user_from_token(token):
    User = get_user_model()
    for user in User.objects.all():
        if account_activation_token.check_token(user, token):
            return user
    return None


@api_view(["GET"])
def verify_email(request):
    token = request.GET.get("token")
    user = get_user_from_token(token)
    if user is not None:
        user.is_active = True
        user.save()
        return Response({"message": "Email verified successfully"}, template_name="email-verified.html", status=200)
    else:
        return Response({"error": "Invalid token"}, template_name="400.html", status=400)


class AccountView(APIView):
    def get(self, request):
        user: User = request.user
        if not user.is_authenticated:
            return redirect("/auth/login")
        if not user.is_active:
            return redirect("/auth/check-email/")
        else:
            profile = request.profile
            return Response({"profile": profile}, template_name="account.html")


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            if user := authenticate(
                request,
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            ):
                login(request, user)
                return redirect("/auth/account/")
        return Response(
            {"serializer": serializer, "profile": request.profile, "invalid": True}, template_name="login.html", status=400
        )

    def get(self, request):
        form = User()
        serializer = UserLoginSerializer(form)
        return Response(
            {"serializer": serializer, "profile": request.profile},
            template_name="login.html",
        )


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(template_name="logged_out.html")


class ResetPasswordView(APIView):
    def post(self, request):
        raise NotImplementedError()

    def get(self, request):
        raise NotImplementedError()
