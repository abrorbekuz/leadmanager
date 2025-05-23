from rest_framework import permissions

class IsAuthenticatedOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and view.action == 'create':
            return True
        return request.user and request.user.is_authenticated