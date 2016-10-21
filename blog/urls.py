from django.conf.urls  import include, url
from . import views 

urlpatterns = [

	url(r'^$',views.post,name='post'),
	url(r'^post/(?P<slug>[\w_-]+)$', views.detail, name='detail'),
	url(r'^post_new/$',views.post_new,name="post_new"),
	url(r'^post/(?P<slug>[\w_-]+)/$', views.comments,name="comment"),
	url(r'^post/(?P<slug>[\w_-]+)/remove/$', views.remove, name='post_remove'),
	url(r'^post/(?P<slug>[\w_-]+)/post_edit/$', views.post_edit,name="post_edit"),
	url(r'^post/(?P<slug>[\w_-]+)$',views.detail),
	url(r'^comment_approve/(?P<pk>[0-9]+)/$',views.comment_approve,name="comment_approve"),
	url(r'^comment_remove/(?P<pk>[0-9]+)/$',views.comment_remove,name="comment_remove"),
	url(r'^post_rascunho/$',views.posts_rascunho,name="post_rascunho"),
	url(r'^post/(?P<slug>[\w_-]+)/pubished/$',views.post_published,name="post_published"),
	url('^sobre-mim/$', views.sobre_mim,name='sobre_mim'),




] 
