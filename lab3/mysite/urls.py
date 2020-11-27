from django.conf.urls import include, url
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url('accounts/', include('accounts.urls')),
	url('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    url(r'', include('blog.urls')),
]