from rest_framework.permissions import BasePermission

class KaprodiPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'DELETE']:
            return request.user and request.user.is_authenticated
        return True
