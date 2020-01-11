
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



from django.conf.urls import url,include
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views 
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('award.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^logout/$', views.logout, {"next_page": '/'}),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^api-token-auth/', obtain_auth_token),
    
]
