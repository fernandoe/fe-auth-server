from django.conf.urls import include, url
from django.contrib import admin
from oauth2_provider.views import TokenView

from fe_auth.introspect import IntrospectTokenView
from fe_auth.views import register

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/v1/introspect/', IntrospectTokenView.as_view(), name='introspect'),
    url(r'^api/v1/register/', register, name='register'),
    url(r'^api/v1/login/', TokenView.as_view(), name='login'),
]
