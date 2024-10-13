from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .consumers import TrngConsumer

@api_view(['GET'])
def ws_status(request: Request):
    # set online to true if any generator is online
    if TrngConsumer.generators > 0:
        online = True
    else:
        online = False
    return Response(data={"online": online}, template_name="ws_status.html")