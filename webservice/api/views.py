import random
from rest_framework.views import APIView
from rest_framework.response import Response
from . import rand

class RandomIntView(APIView):
    def get(self, request):
        n = int(request.query_params.get('n', 1))
        min = int(request.query_params.get('min', 0))
        max = int(request.query_params.get('max', 100))
        return Response(rand.get_int(n, min, max))
    
class RandomFloatView(APIView):
    def get(self, request):
        n = int(request.query_params.get('n', 1))
        precision = int(request.query_params.get('precision', 2))
        return Response(rand.get_float(n, precision))