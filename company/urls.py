from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    url(r'company-list/$', views.CompanyListCreateView.as_view()),
    url(r'company-list/(?P<pk>[0-9]+)/$', views.CompanyRetrieveView.as_view())
    ]
