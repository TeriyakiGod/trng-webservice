from .models import RandTool

def rand_tools(request):
    tools = RandTool.objects.all()
    categories = { tool.category for tool in tools }
    return {'rand_tools': tools, 'categories': categories}