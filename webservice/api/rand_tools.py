from . import serializers, rand, models, points
import datetime


class RandomTool:
    def __init__(self,name, rand_function, serializer, model, point_function):
        self.name = name
        self.rand_function = rand_function
        self.serializer = serializer
        self.model = model
        self.point_function = point_function
        

random_integer = RandomTool("rand_int",rand.get_int, serializers.RandomIntSerializer, models.RandomInt, points.n_points)
random_float = RandomTool("rand_float",rand.get_float, serializers.RandomFloatSerializer, models.RandomFloat, points.n_points)
random_bytes = RandomTool("rand_bytes",rand.get_bytes, serializers.RandomBytesSerializer, models.RandomBytes, points.n_points)
random_string = RandomTool("rand_string",rand.get_strings, serializers.RandomStringSerializer, models.RandomString, points.nm_points)
random_sequence = RandomTool("rand_sequence",rand.get_sequence, serializers.RandomSequenceSerializer, models.RandomSequence, points.minmax_points)
random_coin = RandomTool("rand_coin",rand.get_coin_flips, serializers.RandomCoinSerializer, models.RandomCoin, points.n_points)
random_dice = RandomTool("rand_dice",rand.get_dice_rolls, serializers.RandomDiceSerializer, models.RandomDice, points.nm_points)
random_lotto = RandomTool("rand_lotto",rand.get_lotto, serializers.RandomLottoSerializer, models.RandomLotto, points.n_points)
random_bitmap = RandomTool("rand_bitmap",rand.get_bitmap, serializers.RandomBitmapSerializer, models.RandomBitmap, points.bitmap_points)
random_color = RandomTool("rand_color",rand.get_colors, serializers.RandomColorSerializer, models.RandomColor, points.n_points)

        

class RandomResult:
    def __init__(self, values, points):
        self.values = values
        self.timestamp = datetime.datetime.now().isoformat()
        self.points = points
