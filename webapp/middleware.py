from .models import Visitor

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            x_forwarded_for = request.META.get('X-Forwarded-For')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR')
            visitor, created = Visitor.objects.get_or_create(ip=ip_address)
            request.visitor = visitor

        response = self.get_response(request)
        return response