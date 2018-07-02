from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^sessionwords$', views.index),
    url(r'^sessionwords/add_word$', views.add_word),
    url(r'^sessionwords/clear$', views.clear)
]
