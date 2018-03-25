from django.conf.urls import url
from ideas import views

urlpatterns = [
    url(r'^(?P<idea_id>\d+)$', views.idea_content),
    url(r'^content/(?P<idea_id>\d+)$', views.idea_content_c),
    url(r'^list$', views.idea_list),
    url(r'^editlist$', views.idea_list_for_edit),
    url(r'^edit/(?P<idea_id>\d+)', views.edit_idea),
    url(r'^edit', views.new_idea),
    url(r'^save', views.save_idea),
]
