import asyncio
from django.shortcuts import redirect

from django.urls import reverse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.request import Request
from asgiref.sync import async_to_sync
from . import rand_tools
from .exceptions import ServiceUnavailable
from rest_framework.exceptions import PermissionDenied
from .renderers import ImageRenderer, BinaryRenderer


@api_view(["GET"])
def rand_tool_view(request: Request, tool: rand_tools.RandomTool):
    serialized_request = tool.serializer(data=request.query_params)
    if serialized_request.is_valid(raise_exception=True):
        validated_data = getattr(serialized_request, "validated_data", None)
        if validated_data is not None:
            try:
                points = tool.point_function(request)
                profile = request.profile
                if (profile.points - points) < 0:
                    raise PermissionDenied(
                        "Insufficient points. Bits required: "
                        + str(points)
                        + ", Bits available: "
                        + str(profile.points)
                    )
                result = rand_tools.RandomResult(
                    async_to_sync(tool.rand_function)(**validated_data), points
                )
                profile.points -= points
                profile.save()
            except asyncio.TimeoutError:
                raise ServiceUnavailable()
            return Response(data=vars(result), template_name="random_result.html")


@api_view(["GET"])
@renderer_classes((ImageRenderer,))
def rand_bitmap_view(request: Request, tool: rand_tools.RandomTool):
    serialized_request = tool.serializer(data=request.query_params)
    if serialized_request.is_valid(raise_exception=True):
        validated_data = getattr(serialized_request, "validated_data", None)
        if validated_data is not None:
            try:
                points = tool.point_function(request)
                profile = request.profile
                if (profile.points - points) < 0:
                    return redirect(
                        reverse("api:insufficient_points") + "?points=" + str(points)
                    )
                bitmap = async_to_sync(tool.rand_function)(**validated_data)
                profile.points -= points
                profile.save()
            except asyncio.TimeoutError:
                return redirect(service_unavailable)
            return Response(bitmap)
        
@api_view(["GET"])
@renderer_classes((BinaryRenderer,))
def rand_raw_view(request: Request, tool: rand_tools.RandomTool):
    serialized_request = tool.serializer(data=request.query_params)
    if serialized_request.is_valid(raise_exception=True):
        validated_data = getattr(serialized_request, "validated_data", None)
        if validated_data is not None:
            try:
                points = tool.point_function(request)
                profile = request.profile
                if (profile.points - points) < 0:
                    return redirect(
                        reverse("api:insufficient_points") + "?points=" + str(points)
                    )
                data = async_to_sync(tool.rand_function)(**validated_data)
                profile.points -= points
                profile.save()
            except asyncio.TimeoutError:
                return redirect(service_unavailable)
            response = Response(data, content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename="random.bin"'
            return response


@api_view(["GET"])
def insufficient_points(request: Request):
    points = request.query_params.get("points")
    try:
        if points is None:
            raise ValueError
        points = int(points)
    except ValueError:
        raise PermissionDenied("Invalid points value")
    profile = request.profile
    raise PermissionDenied(
        "Insufficient bits. Bits required: "
        + str(points)
        + ", Bits available: "
        + str(profile.points)
    )


@api_view(["GET"])
def service_unavailable(request: Request):
    raise ServiceUnavailable()
