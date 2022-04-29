from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(required=False)
    password1 = serializers.CharField(max_length=50)
    password2 = serializers.CharField(max_length=50)

    def validate_email(self, email, first_name, last_name):
        if email:
            try:
                if User.objects.get(email=email) is not None:
                    email = f"{first_name}{last_name}@gmail.com"
            except:
                pass
        return email

    def validate_username(self, first_name, last_name):
        if first_name and last_name:
            username = first_name
            try:
                if User.objects.get(username=first_name) is not None:
                    username += f'_{last_name}'

        return username

    def validate_data(self, password1, password2):
        if password1 and password2 and password1!=password2:
            raise _("Passwords doesn't equal to each other.")


