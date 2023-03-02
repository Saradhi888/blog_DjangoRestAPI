from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import APIView


class HelloWorldView(APIView):

    def get(self,request):
        return Response({'message':'Hello World'})

