from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import APIView
from helloworld.serilizers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor


class HelloWorldView(APIView):

    def get(self, request):
        return Response({'message': 'Hello World'})


class Postview(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
