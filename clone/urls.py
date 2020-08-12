from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('register/', user_views.register, name='register'),
    url('profile/', user_views.profile, name='profile'),
    url('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    url(r'^', include('insta.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
