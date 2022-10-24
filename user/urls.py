from django.urls import path
from . import views
from rest_framework.authtoken import views as view


urlpatterns = [
    path("users/register/", views.UserView.as_view()),
    path("users/login/", view.obtain_auth_token),
    path("users/", views.UserViewUsers.as_view()),
    path("users/<int:user_id>/", views.UserDetailView.as_view()),
]
