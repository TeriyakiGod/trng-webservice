from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .consumers import TrngConsumer
from django.core.cache import cache

@api_view(['GET'])
def ws_status(request: Request):
    online = True
    buffer_size = TrngConsumer.get_buffer_size() * 4  # Get current buffer size in bytes
    return Response(data={"online": online, "buffer_size": buffer_size}, template_name="ws_status.html")
