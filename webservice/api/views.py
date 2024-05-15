import asyncio
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from asgiref.sync import async_to_sync
from . import rand, serializers, rand_tools
from .exceptions import ServiceUnavailable
from rest_framework.exceptions import PermissionDenied
from .renderers import ImageRenderer
from rest_framework.decorators import renderer_classes
from . import logger
from webapp.models import Profile, Visitor


@api_view(['GET'])
def rand_tool_view(request: Request, tool: rand_tools.RandomTool):
    serialized_request = tool.serializer(data=request.query_params)
    if serialized_request.is_valid(raise_exception=True):
        validated_data = getattr(serialized_request, 'validated_data', None)
        if validated_data is not None:
            try:
                points = tool.point_function(request)
                if request.user.is_authenticated:
                    profile = Profile.objects.get(user=request.user)
                    if (profile.points - points) < 0:
                        raise PermissionDenied("Insufficient points. Points required: " + str(points) + ", Points available: " + str(profile.points))
                    result = rand_tools.RandomResult(async_to_sync(tool.rand_function)(**validated_data), points)
                    profile.points -= points
                    profile.save()
                else:
                    visitor = Visitor.objects.get(ip_address=request.META.get('REMOTE_ADDR'))
                    if (visitor.points - points) < 0:
                        raise PermissionDenied("Insufficient points. Points required: " + str(points) + ", Points available: " + str(visitor.points))
                    result = rand_tools.RandomResult(async_to_sync(tool.rand_function)(**validated_data), points)
                    visitor.points -= points
                    visitor.save()
            except asyncio.TimeoutError:
                raise ServiceUnavailable()
            return Response(data=vars(result), template_name="random_result.html")
        
@api_view(['GET'])
@renderer_classes((ImageRenderer,))
def rand_bitmap_view(request: Request):
    tool = rand_tools.random_bitmap
    serialized_request = tool.serializer(data=request.query_params)
    if serialized_request.is_valid(raise_exception=True):
        validated_data = getattr(serialized_request, 'validated_data', None)
        if validated_data is not None:
            try:
                points = tool.point_function(request)
                if request.user.is_authenticated:
                    profile = Profile.objects.get(user=request.user)
                    if (profile.points - points) < 0:
                        raise PermissionDenied("Insufficient points. Points required: " + str(points) + ", Points available: " + str(profile.points))
                    bitmap = async_to_sync(tool.rand_function)(**validated_data)
                    profile.points -= points
                    profile.save()
                else:
                    visitor = Visitor.objects.get(ip_address=request.META.get('REMOTE_ADDR'))
                    if (visitor.points - points) < 0:
                        raise PermissionDenied("Insufficient points. Points required: " + str(points) + ", Points available: " + str(visitor.points))
                    bitmap = async_to_sync(tool.rand_function)(**validated_data)
                    visitor.points -= points
                    visitor.save()
            except asyncio.TimeoutError:
                raise ServiceUnavailable()
            return Response(bitmap)