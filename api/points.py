from rest_framework.request import Request

def n_points(request: Request) -> int:
    #Get parameter n
    n = request.query_params.get('n', None)
    if n is None:
        return -1
    try:
        n = int(n)
    except ValueError:
        return -2
    return n * 32
    
def nm_points(request: Request) -> int:
    #Get parameter n
    n = request.query_params.get('n', None)
    m = request.query_params.get('m', None)
    if n is None or m is None:
        return -1
    try:
        n = int(n)
        m = int(m)
    except ValueError:
        return -2
    return n * m * 32

def minmax_points(request: Request) -> int:
    #Get parameter min
    min = request.query_params.get('min', None)
    max = request.query_params.get('max', None)
    if min is None or max is None:
        return -1
    try:
        min = int(min)
        max = int(max)
    except ValueError:
        return -2
    return (max - min + 1) * 32

def bitmap_points(request: Request) -> int:
    #Get parameters width, height, and zoom_factor
    width = request.query_params.get('width', None)
    height = request.query_params.get('height', None)
    zoom_factor = request.query_params.get('zoom_factor', None)
    if width is None or height is None or zoom_factor is None:
        return -1
    try:
        width = int(width)
        height = int(height)
    except ValueError:
        return -2
    total_pixels = width * height
    return total_pixels