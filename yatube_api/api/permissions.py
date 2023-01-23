from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated


class AuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            raise NotAuthenticated
        return obj.author == request.user
