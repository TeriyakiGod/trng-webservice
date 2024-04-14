from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

@api_view(['GET'])
def display_page(request: Request, template: str):
    rand_tools = [
        {"name": "Random Integer", "path": "rand_int", "description": "Generate a random integer."},
        {"name": "Random Float", "path": "rand_float", "description": "Generate a random float."},
        {"name": "Random String", "path": "rand_string", "description": "Generate a random string."},
        {"name": "Random Bytes", "path": "rand_bytes", "description": "Generate random bytes."},
        {"name": "Random Sequence", "path": "rand_sequence", "description": "Generate a random sequence."},
        {"name": "Random Coin", "path": "rand_coin", "description": "Flip a coin."},
        {"name": "Random Dice", "path": "rand_dice", "description": "Roll a dice."},
        {"name": "Random Lotto", "path": "rand_lotto", "description": "Generate a random lotto number."}
    ]
    return Response(template_name=template, data={"rand_tools": rand_tools})