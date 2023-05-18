from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)

        nickname = data.get("nickname")
        user_image = data.get('user_image')
        if nickname:
            user.nickname = nickname
        if user_image:
            user.image = user_image
        user.save()
        return user
