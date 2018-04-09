from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='index'),
    url(r'^input_text/$', views.input_text, name='input_text'),
]
