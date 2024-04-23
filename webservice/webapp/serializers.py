from rest_framework import serializers

class RandomIntForm:
    def __init__(self, n: int, min: int, max: int, repeat: bool = False):
        self.n = n
        self.min = min
        self.max = max
        self.repeat = repeat
        
class RandomIntFormSerializer(serializers.Serializer):
    n = serializers.IntegerField()
    min = serializers.IntegerField()
    max = serializers.IntegerField()
    repeat = serializers.BooleanField()
    
    def create(self, validated_data) -> RandomIntForm:
        return RandomIntForm(**validated_data)

    def update(self, instance, validated_data):
        instance.n = validated_data.get('n', instance.n)
        instance.min = validated_data.get('min', instance.min)
        instance.max = validated_data.get('max', instance.max)
        instance.repeat = validated_data.get('repeat', instance.repeat)
        instance.save()
        return instance
    
    def save(self) -> RandomIntForm:
        return self.create(self.validated_data)