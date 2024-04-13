from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from . import urls

class Index(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request):
        endpoints = [url.name for url in urls.urlpatterns if url.name is not None]
        return Response({'endpoints': endpoints}, template_name="index.html")


class RandIntForm(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request):
        return Response(template_name="forms/int_form.html")