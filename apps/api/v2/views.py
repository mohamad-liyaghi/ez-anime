from rest_framework.viewsets import ModelViewSet
from movie.models import Film


from .seializers.film import MovieListSerializer
from .permissions import MoviePermission

class FilmViewSet(ModelViewSet):
    '''A Viewset for Get/Create/Update/Detail a movie'''
    
    permission_classes = [MoviePermission,]

    def get_serializer_class(self):
        # find appropriate serializer
        if self.action == "list":
            return MovieListSerializer

    def get_queryset(self):
        return Film.objects.all() \
            .order_by('-ratings__average')
