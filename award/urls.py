from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',views.home, name = 'home'),
    url(r'^proile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', vies.createproject, name='createproject'),
    url(r'^search/', views.searchpost, name='searchpost'),
    url(r'^updateprofile$', views.updateprofile, name='prfileupdate'),
    url(r'^rate/(?P<project_id>\d+)',viws.rate_project, name='rate'),
    url(r'^detail/(?P<project_id>\d+)',views.detail, name='detail'),
    url(r'^api/project/$', views.ProjectList.as_view())
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)