from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AvailableApiViews(APIView):
    '''
        All available api routes. 
    '''
    allowed_methods = ('GET',)
    def get(self, request):
        return Response({"Available api list" : "/api/v1/"}, status=status.HTTP_200_OK)