from django.conf.urls import url
from forum.views import topic_detail, topic_list, TopicCreate, TopicEdit
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>\d+)/detail/$', topic_detail, name='topic_detail'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(TopicEdit.as_view()), name='topic_edit'),
    url(r'^$', topic_list, name='topic_list'),
    url(r'^create/$', login_required(TopicCreate.as_view()), name='topic_create'),
]
