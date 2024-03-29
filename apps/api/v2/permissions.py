from rest_framework.permissions import BasePermission

class MoviePermission(BasePermission):
    '''A permission class that let un authenticated users read things
        and authenticated users to write things in db'''

    def has_permission(self, request, view):
        # allow anyone to access lists
        if request.method == "GET":
            return True
        
        if request.method in ["POST", "PATCH", "PUT", "DELETE"]:
            if request.user.is_authenticated:
                return True

            return False
        
class CastPermission(MoviePermission):
    pass

class GenrePermission(MoviePermission):
    pass