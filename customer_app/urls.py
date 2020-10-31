
from django.conf.urls import url
from .views import CustomerSignUpAPIView

urlpatterns =[
     url('signup', CustomerSignUpAPIView.as_view())
]