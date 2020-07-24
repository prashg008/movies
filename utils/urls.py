from rest_framework.routers import SimpleRouter
from .views import RequestCountViewSet


request_count_router = SimpleRouter()
request_count_router.register(r'', RequestCountViewSet)
