from django.urls import path, include
from rest_framework.authtoken import views

from .views import MyProfile

api_urlpatterns = [

    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('my-profile/', MyProfile.as_view()),

    path('api/', include(api_urlpatterns)),

]
