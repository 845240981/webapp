from django.conf.urls import url
from  . import views
from .views import PostListView


urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    url(r'^share/(?P<post_id>\d+)/$', views.post_share, name='post_share'),
    url(r'^post/(?P<post_slug>.*)/$',views.post_detail,name='post_detail'),
    url(r'^search/',views.post_search,name='post_search')

]
