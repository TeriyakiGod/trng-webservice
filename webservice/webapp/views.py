from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from . models import RandTool

@api_view(['GET'])
def display_page(request: Request, template: str):
    tools = RandTool.objects.all().values('name', 'path', 'description')
    
    return Response(template_name=template, data={'rand_tools': tools})

