from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import APIView
from .serilizers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post

class HelloWorldView(APIView):

    def get(self,request):
        return Response({'message':'Hello World'})

class Postview(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer