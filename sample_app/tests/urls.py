from django.conf import settings
from django.conf.urls import include, url

from sample_app.tests import views


urlpatterns = [
    url(r'^diary/', include('sample_app.urls')),
    url(r'^home$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
]
