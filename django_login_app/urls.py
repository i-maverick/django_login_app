from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^app/', include('app.urls')),
    url(r'^login/', auth_views.login, {'template_name': 'admin/login.html'}),
    url(r'^admin/', admin.site.urls),
]
