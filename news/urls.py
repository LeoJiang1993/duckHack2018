from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^$', views.news),
    url(r'^/(?P<news_id>\d+)$', views.news_content),
    url(r'^/content/(?P<news_id>\d+)$',views.news_content_c),
    url(r'^list/(?P<news_topic_id>\d+)$', views.news_list),
    url(r'^list/list$',views.news_list_list),
]
