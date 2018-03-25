from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^sign_in$', views.sign_in),
    url(r'^sign_up$', views.sign_up),
    url(r'^logout$', views.log_out),
    url(r'^create_account$', views.create_account),
    url(r'^modify$', views.modify),
]
