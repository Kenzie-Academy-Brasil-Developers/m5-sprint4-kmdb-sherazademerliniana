from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, Request, Response, status

from user.models import User
from user.permissions import AuthenticatorUser, IsCriticOrOwner
from user.serializers import UserSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCriticOrOwner]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserViewUsers(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AuthenticatorUser]

    def get(self, request: Request) -> Response:
        users = User.objects.all()

        result_page = self.paginate_queryset(users, request, view=self)

        serializer = UserSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
