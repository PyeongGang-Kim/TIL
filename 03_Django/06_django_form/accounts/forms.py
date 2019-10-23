from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', )

class CustomUserCreationForm(UserCreationForm):
    # UserCreationForm의 메타를 상속
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', )