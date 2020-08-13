from django.conf.urls import url
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    url('^$', PostListView.as_view(), name='insta-home'),
    url('^post/<int:pk>$', PostDetailView.as_view(), name='post_detail'),
    url('^post/new/$', PostCreateView.as_view(), name='post-create'),
]
