from ipware import get_client_ip
from webapp.models import Visitor

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip, _ = get_client_ip(request)
        if not request.user.is_authenticated:
            if client_ip is not None:
                visitor_profile, created = Visitor.objects.get_or_create(ip=client_ip)
                request.profile = visitor_profile
        else:
            request.profile = request.user.profile

        response = self.get_response(request)
        return response