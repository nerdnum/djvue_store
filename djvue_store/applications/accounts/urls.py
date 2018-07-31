from django.conf.urls import include, url
from django.contrib.auth import get_user_model

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
                                        PasswordChangeView
from django.shortcuts import reverse
from django.views.generic.base import TemplateView

from registration.backends.hmac.views import ActivationView

from .views import CustomRegistrationView, login_success
from .forms import CustomUserForm

User = get_user_model()

urlpatterns = [

    # This section uses the views and forms from django-register
    url(r'^register/$',
        CustomRegistrationView.as_view(form_class=CustomUserForm),
        name='registration_register'),
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='registration/activation_complete.html'
        ),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>[-:\w]+)/$',
        ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='registration/registration_complete.html'
        ),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='registration/registration_closed.html'
        ),
        name='registration_disallowed'),

    # This section uses the default views and forms from the standard Django implementation
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^login_success/$', TemplateView.as_view(template_name='registration/login_success.html'), name='login_success'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^password/reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'password/reset/done/$', TemplateView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    url(r'password/reset/complete/$', TemplateView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'password/change/$', PasswordChangeView.as_view(), name='password_change'),
    url(r'password/change/done/$', TemplateView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'),

]