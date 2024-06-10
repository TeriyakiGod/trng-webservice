from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Generator

@api_view(['GET'])
def ws_status(request: Request):
    generators = Generator.objects.all()
    # create a generator list but hide the last half of ip address
    for generator in generators:
        generator.ip = generator.ip.rsplit(".", 2)[0] + ".X.X"
    # set online to true if any generator is online
    online = any(generator.online for generator in generators)
    return Response(data={"generators": generators, "online": online}, template_name="ws_status.html")