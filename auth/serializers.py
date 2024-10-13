from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=5,max_length=30, help_text="All alphanumeric characters allowed, must be between 5 and 30 characters long.", style={'placeholder': 'Enter username'})
    email = serializers.EmailField(required=True, help_text="Enter a valid email address.",style={'placeholder': 'Enter email', 'input_type': 'email'})
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(required=True, write_only=True,style={'input_type': 'password'})

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        # It's important to validate the password field using the validate_password method
        validate_password(data['password'])
        return data
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    