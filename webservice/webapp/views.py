from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

from .models import RandTool
from .serializers import RandomIntForm, RandomIntFormSerializer
from django.urls import reverse


@api_view(['GET'])
def display_template(request: Request, template: str):
    return Response(template_name=template)

@api_view(['GET', 'POST'])
def display_random_int_form(request: Request):
    if request.method == 'POST':
        serializer = RandomIntFormSerializer(data=request.data)
        if serializer.is_valid():
            form: RandomIntForm = serializer.save() # type: ignore
            params = "?n={}&min={}&max={}&repeat={}".format(form.n, form.min, form.max, form.repeat)
            return redirect(reverse('api:rand_int') + params, name="Integer", description="Generate random integers")   
    else:
        form = RandomIntForm(n=1, min=0, max=100, repeat=True)
        serializer = RandomIntFormSerializer(form)
        rand_tool = RandTool.objects.get(path="rand_int")
        return Response({
            'serializer': serializer, 
            'form': form,
            'name': rand_tool.name,
            'description': rand_tool.description
            }, template_name='forms/rand_tool_form.html')