from django.conf import settings
import redis


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


def update_count():
    redis_instance.incr("request_count")


def request_count_middleware(get_response):

    def middleware(request):

        update_count()

        response = get_response(request)

        return response

    return middleware
