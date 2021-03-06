"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.post_list,name = 'post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new',views.post_new,name='post_new'),
	path('post/<int:pk>/edit/',views.post_edit,name ='post_edit'),
	path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
	path(r'^post/(?p<pk>\d+)/publish/$',views.post_publish, name='post_publish'),
	path(r'^post/(?p<pk>\d+)/remove/$',views.post_remove, name='post_remove'),
	path(r'^post/(?p<pk>\d+)/comments/$',views.add_comment_to_post,name='add_comment'),
	path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
	
]


