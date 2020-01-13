from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',views.home, name = 'home'),
    path('proile/(?P<username>\w+)', views.profile, name='profile'),
    path('upload/', vies.createproject, name='createproject'),
    path('search/', views.searchpost, name='searchpost'),
    path('updateprofile$', views.updateprofile, name='prfileupdate'),
    url('rate/(?P<project_id>\d+)',viws.rate_project, name='rate'),
    url('detail/(?P<project_id>\d+)',views.detail, name='detail'),
    path('api/project/$', views.ProjectList.as_view())
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
