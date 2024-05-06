from datetime import datetime
from rest_framework import serializers

class RandomInt:
    def __init__(self, values: list[int]):
        self.values = values
        self.timestamp = datetime.now()

class RandomIntSerializer(serializers.Serializer):
    values = serializers.ListField(child=serializers.IntegerField())
    timestamp = serializers.DateTimeField()
    
    
class RandomIntRequest():
    def __init__(self, min: int, max: int, n: int, repeat: bool):
        self.min = min
        self.max = max
        self.n = n
        self.repeat = repeat
    
        
class RandomIntRequestSerializer(serializers.Serializer):
    min = serializers.IntegerField()
    max = serializers.IntegerField()
    n = serializers.IntegerField()
    repeat = serializers.BooleanField()
    
    def validate(self, data):
        if data['min'] >= data['max']:
            raise serializers.ValidationError("min must be less than max")
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        if abs(data['min'] - data['max']) < 2^32:
            raise serializers.ValidationError("difference between max and min must be less than 2^32")
        if data['repeat'] == False and data['n'] > abs(data['max'] - data['min']) + 1:
            raise serializers.ValidationError("n must be less than or equal to max - min + 1 if repeat is False")
        if data['min'] < -2**32 or data['min'] > 2**32 - 1:
            raise serializers.ValidationError("min must be in the range of -2^32 to 2^32 - 1")
        if data['max'] < -2**32 or data['max'] > 2**32 - 1:
            raise serializers.ValidationError("max must be in the range of -2^32 to 2^32 - 1")
        return data
    
class RandomFloat:
    def __init__(self, values: list[float]):
        self.values = values
        self.timestamp = datetime.now()

class RandomFloatSerializer(serializers.Serializer):
    values = serializers.ListField(child=serializers.FloatField())
    timestamp = serializers.DateTimeField()
    
class RandomString:
    def __init__(self, values: list[str]):
        self.values = values
        self.timestamp = datetime.now()

class RandomStringSerializer(serializers.Serializer):
    values = serializers.ListField(child=serializers.CharField())
    timestamp = serializers.DateTimeField()

class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()
    timestamp = serializers.DateTimeField()
    
class IntParametersSerializer(serializers.Serializer):
    min = serializers.IntegerField(required=False)
    max = serializers.IntegerField(required=False)
    n = serializers.IntegerField(required=False)
    
class FloatParametersSerializer(serializers.Serializer):
    precision = serializers.IntegerField(required=False)
    n = serializers.IntegerField(required=False)
    
class BytesParametersSerializer(serializers.Serializer):
    n = serializers.IntegerField(required=False)
    f = serializers.CharField(required=False)