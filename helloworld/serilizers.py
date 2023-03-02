
from rest_framework import serializers
from helloworld.models import Post

class PostSerializer(serializers.Serializer):
    created_by1 = serializers.CharField(source = "created_by.username" , read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_feilds = ('created_by',)

    def create(self, validated_data):
        validated_data['created_by']=self.context['request'].user
        return Post.objects.create(**validated_data)