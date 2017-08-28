from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'startup/$', views.StartupSearchList.as_view(), name='list'),
    url(r'investor/$', views.InvestorSearchList.as_view(), name='investlist'),

    url(r'startup/add/$', views.StartupCreate.as_view(), name='startup_add'),
    url(r'investor/add/$', views.InvestorCreate.as_view(), name='investor_add'),
    # url(r'startup/(?P<pk>[0-9]+)$', views.StartupUpdate.as_view(), name='startup_update'),
    # url(r'startup/(?P<pk>[0-9]+)/delete/$', views.StartupDelete.as_view(), name='startup_delete'),

    url(r'startup/(?P<pk>[0-9]+)$', views.StartupDetail.as_view(), name='detail'),

    # url(r'^search/', views.StartupSearchList.as_view(), name='search'),
]
