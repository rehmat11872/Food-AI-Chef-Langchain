from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "email",
            "password1",
            "password2"
        )
