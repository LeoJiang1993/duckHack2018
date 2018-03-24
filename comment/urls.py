from django.conf.urls import url
from comment import views

urlpatterns = [
    url('^(?P<news_id>\d+)$', views.get_comment),
    url('^comment$', views.comment),
]
