from django.conf.urls import url
from .views import (CreateRequesttAPIView,GetRequestDetailsAPIView,RequestListView)

urlpatterns = [
    url('rform',CreateRequesttAPIView.as_view()),
    url('details/(?P<pk>.+)',GetRequestDetailsAPIView.as_view()),
    url('getRequesList',RequestListView.as_view())
]