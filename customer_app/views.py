from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .serializers import CustomerSignUpSerializer
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
            return Response(response_data.HTTP_201_CREATED)
        else:
            return Response(serializer.errors.HTTP_400_BAD_REQUEST)