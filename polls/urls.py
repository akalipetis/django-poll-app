from django.conf.urls import patterns, url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'api/polls', views.PollViewSet, base_name='poll-api')

urlpatterns = patterns('',
    url(r'^polls/$', views.IndexView.as_view(), name='index'),
    url(r'^polls/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^polls/(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
) + router.urls
