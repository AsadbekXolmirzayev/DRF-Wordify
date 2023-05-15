from rest_framework import generics, permissions
from wordify.models import Article
from wordify.serializers import ArticleGetSerializer


class PopularPostAPIView(generics.ListAPIView):
    queryset = Article.objects.order_by('-views')[:3]
    serializer_class = ArticleGetSerializer
    permission_classes = [permissions.AllowAny]


class LatestPostsListAPIView(generics.ListAPIView):
    queryset = Article.objects.order_by('-id')
    serializer_class = ArticleGetSerializer
