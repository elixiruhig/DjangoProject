from rest_framework.serializers import ModelSerializer

from blogs.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'image',
            'category'
        ]