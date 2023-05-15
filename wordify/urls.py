from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    TagListCreateAPIView,
    ArticleListCreateAPIView, TagRUDAPIView, CategoryRUDAPIView, ArticleRUDAPIView, CommentListCreateAPIView,
    ExtraImageListCreateAPIView, ExtraTextListCreateAPIView
)


urlpatterns = [
    path('category-ls-cr/', CategoryListCreateAPIView.as_view()),
    path('category-rud/<int:pk>/', CategoryRUDAPIView.as_view()),

    path('tag-ls-cr/', TagListCreateAPIView.as_view()),
    path('tag-rud/<int:pk>/', TagRUDAPIView.as_view()),

    path('article-ls-cr/', ArticleListCreateAPIView.as_view()),
    path('article-rud/<int:pk>/', ArticleRUDAPIView.as_view()),

    path('article/<int:article_id>/comment-ls-cr/', CommentListCreateAPIView.as_view()),

    path('article/<int:article_id>/extra-text/', ExtraTextListCreateAPIView.as_view()),
    path('article/<int:article_id>/extra-image/', ExtraImageListCreateAPIView.as_view()),

]
