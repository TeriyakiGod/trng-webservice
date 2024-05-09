from random import Random
from rest_framework import serializers
from . import UINT32_MAX
from .models import BytesFormat, RandomInt, RandomFloat, RandomString, RandomBytes, RandomSequence, RandomCoin, RandomDice, RandomLotto
       
        
class RandomIntSerializer(serializers.Serializer):
    n = serializers.IntegerField(max_value=10000, min_value=1, label="Count") #TODO: Fix forms
    min = serializers.IntegerField()
    max = serializers.IntegerField()
    repeat = serializers.BooleanField()
    
    def create(self, validated_data):
        return RandomInt(**validated_data)
    
    def validate(self, data):
        if data['min'] >= data['max']:
            raise serializers.ValidationError("min must be less than max")
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        if abs(data['min'] - data['max']) > UINT32_MAX:
            raise serializers.ValidationError("difference between max and min must be less than 2^32")
        if data['repeat'] == False and data['n'] > abs(data['max'] - data['min']) + 1:
            raise serializers.ValidationError("n must be less than or equal to max - min + 1 if repeat is False")
        if data['min'] < -UINT32_MAX or data['min'] > UINT32_MAX:
            raise serializers.ValidationError("min must be in the range of -2^32 to 2^32 - 1")
        if data['max'] < -UINT32_MAX or data['max'] > UINT32_MAX:
            raise serializers.ValidationError("max must be in the range of -2^32 to 2^32 - 1")
        return data
        
class RandomFloatSerializer(serializers.Serializer):
    n = serializers.IntegerField()
    precision = serializers.IntegerField()
    
    def create(self, validated_data):
        return RandomFloat(**validated_data)
    
    def validate(self, data):
        if data['precision'] < 0:
            raise serializers.ValidationError("precision must be greater than or equal to 0")
        if data['precision'] > 9:
            raise serializers.ValidationError("precision must be less than 10")
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        return data
    
class RandomStringSerializer(serializers.Serializer):
    n = serializers.IntegerField()
    m = serializers.IntegerField()
    digits = serializers.BooleanField()
    letters = serializers.BooleanField()
    special = serializers.BooleanField()
    repeat = serializers.BooleanField()
    
    def create(self, validated_data):
        return RandomString(**validated_data)
    
    def validate(self, data):
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        if data['m'] < 1:
            raise serializers.ValidationError("m must be greater than 0")
        if data['m'] > 100:
            raise serializers.ValidationError("m must be less than 100")
        if not (data['digits'] or data['letters'] or data['special']):
            raise serializers.ValidationError("at least one of digits, letters, or special must be True")
        if not data['repeat'] and data['digits'] and data['letters'] and data['special']:
            if data['m'] > 95:
                raise serializers.ValidationError("m must be less than or equal to 95 if repeat is False and digits, letters, and special are True")
        elif not data['repeat'] and data['digits'] and data['letters']:
            if data['m'] > 62:
                raise serializers.ValidationError("m must be less than or equal to 62 if repeat is False and digits and letters are True")
        elif not data['repeat'] and data['digits'] and data['special']:
            if data['m'] > 43:
                raise serializers.ValidationError("m must be less than or equal to 43 if repeat is False and digits and special are True")
        elif not data['repeat'] and data['letters'] and data['special']:
            if data['m'] > 85:
                raise serializers.ValidationError("m must be less than or equal to 85 if repeat is False and letters and special are True")
        elif not data['repeat'] and data['digits']:
            if data['m'] > 10:
                raise serializers.ValidationError("m must be less than or equal to 10 if repeat is False and digits is True")
        elif not data['repeat'] and data['letters']:
            if data['m'] > 52:
                raise serializers.ValidationError("m must be less than or equal to 52 if repeat is False and letters is True")
        elif not data['repeat'] and data['special']:
            if data['m'] > 33:
                raise serializers.ValidationError("m must be less than or equal to 33 if repeat is False and special is True") 
        return data

class RandomBytesSerializer(serializers.Serializer):
    n = serializers.IntegerField()
    f = serializers.ChoiceField(choices=[(format.value, format.name) for format in BytesFormat])
    
    def create(self, validated_data):
        return RandomBytes(**validated_data)
    
    def validate(self, data):
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        if data['f'] not in ['h', 'o', 'b', 'd']:
            raise serializers.ValidationError("f must be one of ['h', 'o', 'b', 'd']")
        return data
    
class RandomSequenceSerializer(serializers.Serializer):
    min = serializers.IntegerField()
    max = serializers.IntegerField()
    
    def create(self, validated_data):
        return RandomSequence(**validated_data)
    
    def validate(self, data):
        if data['min'] >= data['max']:
            raise serializers.ValidationError("min must be less than max")
        if abs(data['min'] - data['max']) < 2^32:
            raise serializers.ValidationError("difference between max and min must be less than 2^32")
        if data['min'] < -UINT32_MAX or data['min'] > UINT32_MAX:
            raise serializers.ValidationError("min must be in the range of -2^32 to 2^32 - 1")
        if data['max'] < -UINT32_MAX or data['max'] > UINT32_MAX:
            raise serializers.ValidationError("max must be in the range of -2^32 to 2^32 - 1")
        return data
    
class RandomCoinSerializer(serializers.Serializer):
    n = serializers.IntegerField()
    
    def create(self, validated_data):
        return RandomCoin(**validated_data)
    
    def validate(self, data):
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        return data
    
class RandomDiceSerializer(serializers.Serializer):
    n = serializers.IntegerField()
    m = serializers.IntegerField()
    
    def create(self, validated_data):
        return RandomDice(**validated_data)
    
    def validate(self, data):
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        if data['m'] < 1:
            raise serializers.ValidationError("m must be greater than 0")
        if data['m'] > 100:
            raise serializers.ValidationError("m must be less than 100")
        return data
    
class RandomLottoSerializer(serializers.Serializer):
    n = serializers.IntegerField()
    
    def create(self, validated_data):
        return RandomLotto(**validated_data)
    
    def validate(self, data):
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        return data

class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()
    timestamp = serializers.DateTimeField()