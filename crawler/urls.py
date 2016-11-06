from django.conf.urls import url

from . import views

app_name = 'crawler'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_url_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<item_url_id>[0-9]+)/download/$', views.download, name='download'),
]