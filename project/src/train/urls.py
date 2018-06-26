from django.conf.urls import url
from train.views import training_list, training_detail

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', training_detail, name='training_detail'),
    url(r'$', training_list, name='training_list'),
]