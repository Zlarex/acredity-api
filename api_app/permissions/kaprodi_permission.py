from rest_framework.permissions import BasePermission

class KaprodiPermission(BasePermission):
  def has_permission(self, request, view):
    return request.user and request.user.is_authenticated