from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,GenericAPIView

from .serializers import CustomerSignUpSerializer ,CustomerLoginSerializer
from .models import Customer


class CustomerSignUpAPIView(CreateAPIView):
    serializer_class = CustomerSignUpSerializer

    def post(self,request, *args, **kwargs):

        print("REQUESTED DATA",request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            #if valid then it works as insert()
            serializer.save()

            #taking email_id from requested data and put in email field
            obj=Customer.objects.get(email=request.data["email"])

            response_data = {
                "id":obj.id,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
                "email":obj.email
            }
            return Response(response_data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class CustomerLoginpAPIView(GenericAPIView):
    serializer_class = CustomerLoginSerializer

    def post(self,request,*args,**kwargs):
        print("REQUSTED DATA",request.data)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            obj = serializer.user

            if request.data["type_user"]==obj.type_c:

                response_data ={
                "first_name":obj.first_name,
                "id":obj.id,
                "last_name":obj.last_name,
                "Email Adress":obj.email
                }

                return Response(response_data,status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
