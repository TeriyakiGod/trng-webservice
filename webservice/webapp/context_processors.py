from .models import RandTool

def rand_tools(request):
    tools = RandTool.objects.all()
    return {'rand_tools': tools}