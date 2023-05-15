from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Article, Category, Tag, Comment, ExtraText, ExtraImage

from .serializers import CategorySerializer, TagSerializer, ArticleGetSerializer, ArticlePostSerializer, \
    CommentSerializer, ExtraImageSerializer, ExtraTextSerializer, MineExtraTextSerializer
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CategorySerializer


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        if self.request.method == 'POST':
            return ArticlePostSerializer
        return Response({'detail': "Method, not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ArticleRUDAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer


class ExtraTextListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExtraText.objects.all()

    def get_queryset(self, *args, **kwargs):
        text = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            text = text.filter(article_id=article_id)
            return text
        return []

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MineExtraTextSerializer
        return ExtraTextSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx


class ExtraImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExtraImage.objects.all()
    serializer_class = ExtraImageSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx



