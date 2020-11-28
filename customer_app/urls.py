
from django.conf.urls import url
from .views import CustomerSignUpAPIView ,CustomerLoginpAPIView

urlpatterns =[
     url('signup', CustomerSignUpAPIView.as_view()),
     url('login',CustomerLoginpAPIView.as_view()) ,
]