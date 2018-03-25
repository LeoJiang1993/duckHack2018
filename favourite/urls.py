from django.conf.urls import url
from favourite import views

urlpatterns = [
    url(r'^unlike/(?P<idea_id>\d+)$', views.unlike),
    url(r'^like/(?P<idea_id>\d+)$', views.like),
    url(r'^bar/(?P<idea_id>\d+)', views.bar),
    url(r'^list', views.get_list),
]
