from django.conf import settings
from django.shortcuts import render
from registration.backends.hmac.views import RegistrationView
from django.conf import settings

class CustomRegistrationView(RegistrationView):

    def get_email_context(self, activation_key):
        email_context = super(CustomRegistrationView, self).get_email_context(activation_key=activation_key)
        email_context['scheme'] = settings.HTTP_PREFIX
        return email_context

def login_success(request):
    return render(request, template_name='registration/login_success.html')
