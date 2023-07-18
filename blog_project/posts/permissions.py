from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # tolka korush uchun uruksat
        if request.method in permissions.SAFE_METHODS:
            return True

        # ozgortush uchun jana jathish uchun uruksat jalan post eelerine berilet
        return obj.auther == request.user
