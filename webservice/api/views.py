from rest_framework.views import APIView
from rest_framework.response import Response
from trng.interface import rng


def rand_int_range(range):
    # Debiased Integer Multiplication — Lemire's Method
    t = (-range) % range
    while True:
        x = rng()
        m = x * range
        l = m & 0xFFFFFFFF
        if l >= t:
            break
    return m >> 32

class RandomNumberView(APIView):
    
    def get(self, request):
        n = int(request.query_params.get('n', 1))
        a = int(request.query_params.get('a', 0))
        b = int(request.query_params.get('b', 100))

        # Get the random numbers from the buffer
        random_numbers = []
        for _ in range(n):
            random_number = rand_int_range(b - a) + a
            random_numbers.append(random_number)

        return Response(random_numbers)