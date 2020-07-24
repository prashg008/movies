import redis
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


@permission_classes(['AllowAny'])
@api_view()
def request_count(request):
    count = redis_instance.get("request_count")
    if count:
        return Response({"requests": count})


@permission_classes(['AllowAny'])
@api_view(['POST'])
def reset_request_count(request):
    redis_instance.delete("request_count")
    return Response({"message": "request count reset successfully"})
