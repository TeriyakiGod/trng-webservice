from .models import RandTool, Visitor

def rand_tools(request):
    tools = RandTool.objects.all()
    categories = { tool.category for tool in tools }
    visitor = Visitor.objects.get(ip=request.META.get('REMOTE_ADDR'))
    return {'rand_tools': tools, 'categories': categories, 'visitor': visitor}