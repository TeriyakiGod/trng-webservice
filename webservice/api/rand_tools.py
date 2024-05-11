import random
from . import serializers, rand, models
import datetime

class RandomTool:
    def __init__(self,name, rand_function, serializer, model):
        self.name = name
        self.rand_function = rand_function
        self.serializer = serializer
        self.model = model
        

random_integer = RandomTool("rand_int",rand.get_int, serializers.RandomIntSerializer, models.RandomInt)
random_float = RandomTool("rand_float",rand.get_float, serializers.RandomFloatSerializer, models.RandomFloat)
random_string = RandomTool("rand_string",rand.get_strings, serializers.RandomStringSerializer, models.RandomString)
random_bytes = RandomTool("rand_bytes",rand.get_bytes, serializers.RandomBytesSerializer, models.RandomBytes)
random_sequence = RandomTool("rand_sequence",rand.get_sequence, serializers.RandomSequenceSerializer, models.RandomSequence)
random_coin = RandomTool("rand_coin",rand.get_coin_flips, serializers.RandomCoinSerializer, models.RandomCoin)
random_dice = RandomTool("rand_dice",rand.get_dice_rolls, serializers.RandomDiceSerializer, models.RandomDice)
random_lotto = RandomTool("rand_lotto",rand.get_lotto, serializers.RandomLottoSerializer, models.RandomLotto)
random_bitmap = RandomTool("rand_bitmap",rand.get_bitmap, serializers.RandomBitmapSerializer, models.RandomBitmap)
random_color = RandomTool("rand_color",rand.get_colors, serializers.RandomColorSerializer, models.RandomColor)
        


class RandomResult:
    def __init__(self, values):
        self.values = values
        self.timestamp = datetime.datetime.now().isoformat()
