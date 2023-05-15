from django.urls import path
from .views import PopularPostAPIView, LatestPostsListAPIView

urlpatterns = [
    path('popular-posts/', PopularPostAPIView.as_view()),
    path('latest-posts/', LatestPostsListAPIView.as_view()),
]
