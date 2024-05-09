from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

from api.rand_tools import RandomTool
from .models import RandTool
from django.urls import reverse

@api_view(['GET'])
def template_view(request: Request, template: str):
    return Response(template_name=template)
        
@api_view(['GET', 'POST'])
def random_tool_form_view(request: Request, tool: RandomTool):
    if request.method == 'POST':
        serializer = tool.serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serialized_form = serializer.save()
            dict = vars(serialized_form)
            params = "?"
            for key in dict:
                params += "{}={}&".format(key, dict[key])
            return redirect(reverse('api:' + tool.name) + params)
    else:
        form = tool.model()
        serializer = tool.serializer(form)
        rand_tool = RandTool.objects.get(path=tool.name)
        return Response({
            'serializer': serializer,
            'name': rand_tool.name,
            'description': rand_tool.description
            }, template_name='rand_tool_form.html')
        