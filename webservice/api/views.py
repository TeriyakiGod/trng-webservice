from rest_framework.views import APIView
from rest_framework.response import Response
from . import rand

class RandomIntView(APIView):
    def get(self, request):
        n = int(request.query_params.get('n', 1))
        if n <= 0:
            return Response({"error": "Invalid n. Must be greater than 0"}, status=400)
        if n > 1024:
            return Response({"error": "Invalid n. Must be less than or equal to 1024"}, status=400)
        min = int(request.query_params.get('min', 0))
        max = int(request.query_params.get('max', 100))
        return Response(rand.get_int(n, min, max))
    
class RandomFloatView(APIView):
    def get(self, request):
        n = int(request.query_params.get('n', 1))
        if n <= 0:
            return Response({"error": "Invalid n. Must be greater than 0"}, status=400)
        if n > 1024:
            return Response({"error": "Invalid n. Must be less than or equal to 1024"}, status=400)
        p = int(request.query_params.get('precision', 2))
        return Response(rand.get_float(n, p))
    
class RandomBytesView(APIView):
    def get(self, request):
        n = int(request.query_params.get('n', 4))
        if n <= 0:
            return Response({"error": "Invalid n. Must be greater than 0"}, status=400)
        if n > 1024:
            return Response({"error": "Invalid n. Must be less than or equal to 1024"}, status=400)
        f = str(request.query_params.get('f', 'h'))
        if f not in ['h', 'o', 'b', 'd']:
            return Response({"error": "Invalid format. Must be one of ['h', 'o', 'b', 'd']"}, status=400)
        return Response(rand.get_bytes(n, f))
    
class TestView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})