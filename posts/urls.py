from django.conf.urls import url, include
from django.contrib import admin
from .views import index, create_post, post_detail, edit_post

# different urlpatterns use different methods from the views.
urlpatterns = [
    url(r'^$', index),
    url(r'^create',create_post),
    url(r'^post/(?P<post_id>\d+)', post_detail),
    url(r'^edit/(?P<post_id>\d+)', edit_post),
]
