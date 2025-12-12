from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsRoleAllowed(permissions.BasePermission):
    """
    Generic permission: views should set view.allowed_roles = ['kassir', 'omborchi']
    SAFE_METHODS allowed for everyone (including anonymous). For unsafe methods, check role or superuser.
    """
    def has_permission(self, request, view):
        # Allow all safe (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # For unsafe methods require authentication
        if not request.user or not request.user.is_authenticated:
            return False

        # Superuser bypass
        if request.user.is_superuser:
            return True

        allowed = getattr(view, "allowed_roles", None)
        if not allowed:
            # if allowed_roles not set, fallback to staff only
            return request.user.is_staff

        # assume user has attribute 'role' (string)
        user_role = getattr(request.user, "role", None)
        return user_role in allowed
