from __future__ import unicode_literals

from rest_framework.permissions import BasePermission


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a staff user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )