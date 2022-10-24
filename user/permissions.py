from rest_framework import permissions
from rest_framework.views import Request, View

from user.models import User


class AuthenticatorUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated and request.user.is_superuser


class IsCriticOrOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        if request.user == obj or request.user.is_superuser == True:
            return True
