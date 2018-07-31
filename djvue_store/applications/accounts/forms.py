from django.contrib.auth import get_user_model
from registration.forms import RegistrationForm

User = get_user_model()

class CustomUserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ('email', 'username',)