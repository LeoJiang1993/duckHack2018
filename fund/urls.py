from django.conf.urls import url
from fund import views

urlpatterns = [
    url(r'^fonder/(?P<user_id>\d+)$', views.get_fund_by_fonder),
    url(r'^idea/(?P<idea_id>\d+)$', views.get_fund_by_idea),
    url(r'^make', views.make_fund),
    url(r'^my',views.get_fund_by_fonder)
]
