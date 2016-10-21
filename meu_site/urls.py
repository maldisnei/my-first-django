from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'', include('blog.urls')),
	url('^accounts/login/$',views.login, name="login"),
	url('^accounts/logout/$',views.logout, name="logout", kwargs={'next_page': '/'}),
	
]
