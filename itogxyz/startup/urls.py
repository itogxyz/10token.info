from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.StartupSearchList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)$', views.StartupDetail.as_view(), name='detail'),
    # url(r'^search/', views.StartupSearchList.as_view(), name='search'),
]
