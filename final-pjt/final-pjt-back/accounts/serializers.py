from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    nickname = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'password1', 'password2', 'token']

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs
    
    def validate_email(self, value):
        user_model = self.Meta.model
        if user_model.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address is already in use.")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from validated_data
        password = validated_data.pop('password1')  # Retrieve password1
        validated_data['password'] = make_password(password)  # Hash the password
        user = User.objects.create_user(**validated_data)
        return user

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key
