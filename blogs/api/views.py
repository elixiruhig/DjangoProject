from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from blogs.api.serializers import PostSerializer, CreateUpdateSerializer
from blogs.models import Post


class PostListAPIView(ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','body','category']

class PostDetailAPIView(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

class PostUpdateAPIView(UpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = CreateUpdateSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

class PostDeleteAPIView(DestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

class PostCreateAPIView(CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = CreateUpdateSerializer