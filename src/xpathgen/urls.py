from django.conf.urls import url
from .views import XPathGenView


urlpatterns = [
    url(r'$', XPathGenView.as_view(), name='XPathView'),
]
