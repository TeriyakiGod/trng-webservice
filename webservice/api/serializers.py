from datetime import datetime
from rest_framework import serializers

class RandomInt:
    def __init__(self, values: list[int]):
        self.values = values
        self.timestamp = datetime.now()

class RandomIntSerializer(serializers.Serializer):
    values = serializers.ListField(child=serializers.IntegerField())
    timestamp = serializers.DateTimeField()
    
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