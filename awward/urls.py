from django.conf.urls import url,include
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views 
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('award.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api-token-auth/', obtain_auth_token),
    
]
