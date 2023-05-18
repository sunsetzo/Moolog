from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer, PasswordChangeSerializer

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
    user_image = serializers.CharField(max_length=500)
    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'user_image')
        read_only_fields = ('username', 'email')

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
    

class CustomPasswordChangeSerializer(PasswordChangeSerializer):
    
    def validate(self, attrs):
        attrs = super().validate(attrs)

        old_password = attrs.get('old_password')
        new_password1 = attrs.get('new_password1')
        new_password2 = attrs.get('new_password2')

        if old_password and new_password1 and old_password == new_password1:
            raise serializers.ValidationError("새로운 비밀번호는 기존 비밀번호와 동일한 것을 사용할 수 없습니다.")

        return attrs