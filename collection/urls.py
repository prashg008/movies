from rest_framework.routers import SimpleRouter
from .views import CollectionViewSet

collection_router = SimpleRouter()
collection_router.register(r'collection', CollectionViewSet)