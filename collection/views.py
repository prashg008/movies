import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.auth import HTTPBasicAuth

from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Collections
from .serializers import CollectionsSerializer


@permission_classes(['IsAuthenticated'])
@api_view()
def movies_list(request):
    username = 'iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0'
    password = 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'
    retry_strategy = Retry(total=10,
                           status_forcelist=[429, 500, 502, 503, 504],
                           method_whitelist=["HEAD", "GET", "OPTIONS"]
                        )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)
    auth=HTTPBasicAuth(username, password)

    response = http.get("https://demo.credy.in/api/v1/maya/movies/", auth=auth)

    return Response(response.json())


class CollectionViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = CollectionsSerializer
    queryset = Collections.objects.all()
    lookup_field = 'uuid'

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(owner=self.request.user)


    def list(self, request):
        queryset = self.get_queryset()
        serialized_data = self.serializer_class(queryset, many=True)
        response = {
            'is_success': True,
            'data': {
                'collections': serialized_data.data
            }
        }
        return Response(response)

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'collection_uuid': serializer.instance.uuid})
