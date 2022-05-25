from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        age = data.get("age")
        gender = data.get("gender")
        if age:
            user.age = age

        if gender:
            user.gender = gender

        user.save()
        return user