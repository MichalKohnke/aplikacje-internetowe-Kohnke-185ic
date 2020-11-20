from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url('accounts/', include('accounts.urls')),
	url('accounts/', include('django.contrib.auth.urls')),   
    url(r'', include('blog.urls')),
]