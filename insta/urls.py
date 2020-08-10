from django.conf.urls import url
from . import views

urlpatterns=[
    
    url('^today/$',views.posts_today,name='postsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_posts,name = 'pastPosts'),
    url(r'^search/', views.search_results, name='search_results')
]