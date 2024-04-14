from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

@api_view(['GET'])
def index(request: Request):
    return Response(template_name="index.html")

@api_view(['GET'])
def about(request: Request):
    return Response(template_name="about.html")

@api_view(['GET'])
def rand_int_form(request: Request):
    return Response(template_name="forms/int_form.html")