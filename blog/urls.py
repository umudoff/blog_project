from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^edit_post/(?P<posid>[-\w]+)/$', views.edit_post, name='edit_post'),
        url(r'^edit_comment/(?P<comid>[-\w]+)/$', views.edit_comment, name='edit_comment'),
        url(r'^added/$', views.added, name= 'added'),
        url(r'^posts/add_post/$', views.add_post, name='add_post'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^posts/$',views.posts, name='posts'),
        url(r'^posts/(?P<posid>[-\w]+)/$', views.add_comment, name='add_comment'),
       
              )