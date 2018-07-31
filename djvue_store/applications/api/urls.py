from django.conf.urls import url, include
from rest_framework.authtoken import views as auth_views

from .views import CustomObtainAuthToken, UserDetail

urlpatterns = [
    url(r'^get_auth_token/$', CustomObtainAuthToken.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name=UserDetail.name)
]

