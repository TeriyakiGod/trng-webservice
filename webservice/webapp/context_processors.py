from .models import RandTool

def rand_tools(request):
    tools = RandTool.objects.all().values('name', 'path', 'description')
    return {'rand_tools': tools}