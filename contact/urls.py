from django.urls import path
from .views import ContactListCreateAPIView


urlpatterns = [
    path('list-create/', ContactListCreateAPIView.as_view()),

]