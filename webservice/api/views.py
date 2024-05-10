import asyncio
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from asgiref.sync import async_to_sync
from . import rand, serializers, rand_tools
from .exceptions import ServiceUnavailable
from .renderers import ImageRenderer
from rest_framework.decorators import renderer_classes
from . import logger
from webapp.models import Profile, Visitor


@api_view(['GET'])
def rand_tool_view(request: Request, tool: rand_tools.RandomTool):
    required_points = 0
    #Come up with a better way to do this
    if request.path == '/api/rand/int':
        n = request.GET.get('n')
        if n:
            n = int(n)
            required_points = n * 8

        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            if profile.points >= required_points:
                profile.points = profile.points - required_points
                profile.save()
                logger.info(f"{request.user.username} used {required_points} points. They have {profile.points} left.")
            else:
                return Response({'errors': ["Not enough points. Get more points."]}, template_name="403.html", status=403)
        else:
            ip_address = request.META.get('REMOTE_ADDR')
            visitor = Visitor.objects.get(ip=ip_address)
            if visitor.points >= required_points:
                visitor.points = visitor.points - required_points
                logger.info(f"{visitor.ip} used {required_points} points. They have {visitor.points} left.")
                visitor.save()
            else:
                return Response({'errors': ["Not enough points. Get more points."]}, template_name="403.html", status=403)
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