from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer, PasswordChangeSerializer

User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):

    # followings = serializers.SerializerMethodField()

    # def get_followings(self, obj):
    #     # 현재 유저의 followings를 가져와서 유저의 pk값만 리스트로 반환
    #     return UserSerializer(obj.followings.all(), many=True).data

    # class Meta:
    #     model = User
    #     fields = ('id', )

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
    nickname = serializers.CharField(max_length=20, required=False)
    user_image = serializers.ImageField(required=False)


    followings = serializers.ManyRelatedField(child_relation=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()), source='followings.all', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)
    followers = serializers.ManyRelatedField(child_relation=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()), source='followers.all', read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)    


    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'user_image', 'followings', 'followings_count', 'followers', 'followers_count')
        read_only_fields = ('username','email')

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname','')
        data['user_image'] = self.validated_data.get('user_image', '')
        return data

    def validate_nickname(self, value):
        user_model = self.Meta.model
        # 현재 요청을 보낸 유저
        user = self.context['request'].user
        # 해당 닉네임이 존재하고 그 닉네임이 회원 정보 수정을 요청한 유저의 닉네임이 아닐 경우 에러 발생
        if user_model.objects.exclude(id=user.id).filter(nickname=value).exists():
            raise serializers.ValidationError("다른 유저가 사용 중인 닉네임 입니다. 다른 닉네임을 입력해주세요.")
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