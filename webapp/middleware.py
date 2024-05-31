from .models import Visitor

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            ip_address = request.META.get('REMOTE_ADDR')
            visitor, created = Visitor.objects.get_or_create(ip=ip_address)
            request.visitor = visitor

        response = self.get_response(request)
        return response