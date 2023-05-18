from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = '__all__'

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname','')
        return data
    
    def validate_nickname(self, value):
        user_model = self.Meta.model
        if user_model.objects.filter(nickname=value).exists():
            raise serializers.ValidationError("사용 중인 닉네임 입니다. 다른 닉네임을 입력해주세요.")
        return value
    

class CustomUserDetailsSerializer(UserDetailsSerializer):
    nickname = serializers.CharField(max_length=20)
    user_image = serializers.ImageField

    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'user_image')

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname','')
        data['user_image'] = self.validated_data.get('user_image', '')
        return data

    def validate_nickname(self, value):
        user_model = self.Meta.model
        if user_model.objects.filter(nickname=value).exists():
            raise serializers.ValidationError("사용 중인 닉네임 입니다. 다른 닉네임을 입력해주세요.")
        return value