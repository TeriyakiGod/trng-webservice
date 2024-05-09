import asyncio
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from asgiref.sync import async_to_sync
from . import rand, serializers, rand_tools
from .exceptions import ServiceUnavailable
from django.http import FileResponse
from .renderers import ImageRenderer
from rest_framework.decorators import renderer_classes


@api_view(['GET'])
def rand_tool_view(request: Request, tool: rand_tools.RandomTool):
    serialized_request = tool.serializer(data=request.query_params)
    if serialized_request.is_valid(raise_exception=True):
        validated_data = getattr(serialized_request, 'validated_data', None)
        if validated_data is not None:
            try:
                result = rand_tools.RandomResult(async_to_sync(tool.rand_function)(**validated_data))
            except asyncio.TimeoutError:
                raise ServiceUnavailable()
            return Response(data=vars(result), template_name="random_result.html")
        
@api_view(['GET'])
@renderer_classes((ImageRenderer,))
def rand_bitmap_view(request: Request):
    serialized_request = serializers.RandomBitmapSerializer(data=request.query_params)
    if serialized_request.is_valid(raise_exception=True):
        validated_data = getattr(serialized_request, 'validated_data', None)
        if validated_data is not None:
            try:
                bitmap = async_to_sync(rand.get_bitmap)(**validated_data)
            except asyncio.TimeoutError:
                raise ServiceUnavailable()
            return Response(bitmap)