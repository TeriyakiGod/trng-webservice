from turtle import width
from rest_framework import serializers
from . import UINT32_MAX
from .models import BytesFormat, RandomInt, RandomFloat, RandomString, RandomBytes, RandomSequence, RandomCoin, RandomDice, RandomLotto, RandomBitmap, RandomColor
       
        
class RandomIntSerializer(serializers.Serializer):
    n = serializers.IntegerField(label="N", help_text="Number of random integers to generate (1 to 10000)")
    min = serializers.IntegerField(label="Minimum value", help_text="Minimum value of the random integers (-2^32 to 2^32 - 1)")
    max = serializers.IntegerField(label="Maximum value", help_text="Maximum value of the random integers (-2^32 to 2^32 - 1)")
    repeat = serializers.BooleanField(label="Allow repeated values", help_text="Check if you want values to repeat")
    
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
    n = serializers.IntegerField(label="N", help_text="Number of random floats to generate (1 to 10000)")
    precision = serializers.IntegerField(label="Precision", help_text="Number of decimal places (1 to 9)")
    
    def create(self, validated_data):
        return RandomFloat(**validated_data)
    
    def validate(self, data):
        if data['precision'] < 1:
            raise serializers.ValidationError("precision must be greater than or equal to 1")
        if data['precision'] > 9:
            raise serializers.ValidationError("precision must be less than 10")
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        return data
    
class RandomStringSerializer(serializers.Serializer):
    n = serializers.IntegerField(label="N", help_text="Number of random strings to generate (1 to 10000)")
    m = serializers.IntegerField(label="M", help_text="Length of the random strings (1 to 100)")
    digits = serializers.BooleanField(label="Digits", help_text="Check if you want digits in the random strings")
    letters = serializers.BooleanField(label="Letters", help_text="Check if you want letters in the random strings")
    special = serializers.BooleanField(label="Special characters", help_text="Check if you want special characters in the random strings")
    repeat = serializers.BooleanField(label="Allow repeated values", help_text="Check if you want values to repeat")
    
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
    n = serializers.IntegerField(label="N", help_text="Number of random bytes to generate (1 to 10000)")
    f = serializers.ChoiceField(label="Numeral system",choices=[(format.value, format.name) for format in BytesFormat], help_text="Choose the numeral system for the random bytes to be represented in")
    
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
    min = serializers.IntegerField(label="Minimum value", help_text="Minimum value of the random sequence (-2^32 to 2^32 - 1)")
    max = serializers.IntegerField(label="Maximum value", help_text="Maximum value of the random sequence (-2^32 to 2^32 - 1)")
    
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
    n = serializers.IntegerField(label="N", help_text="Number of random coin flips to generate (1 to 10000)")
    
    def create(self, validated_data):
        return RandomCoin(**validated_data)
    
    def validate(self, data):
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        return data
    
class RandomDiceSerializer(serializers.Serializer):
    n = serializers.IntegerField(label="N", help_text="Number of random dice rolls to generate (1 to 10000)")
    m = serializers.IntegerField(label="Sides", help_text="Number of sides on the dice (1 to 100)")
    
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
    n = serializers.IntegerField(label="N", help_text="Number of random lotto tickets to generate (1 to 10000)")
    
    def create(self, validated_data):
        return RandomLotto(**validated_data)
    
    def validate(self, data):
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        return data

class RandomBitmapSerializer(serializers.Serializer):
    width = serializers.IntegerField(label="Width", help_text="Width of the bitmap (1 to 512)")
    height = serializers.IntegerField(label="Height", help_text="Height of the bitmap (1 to 512)")
    zoom_factor = serializers.IntegerField(label="Zoom", help_text="How many times should the image be enlarged (1 to 16). <br><br> The final image resolution is width * zoom x height * zoom. <br><br> <div class='alert alert-warning' role='alert'>Warning: it may take couple seconds for the image to be generated.</div>")
    
    def create(self, validated_data):
        return RandomBitmap(**validated_data)
    
    def validate(self, data):
        if data['width'] < 1:
            raise serializers.ValidationError("width must be greater than 0")
        if data['width'] > 512:
            raise serializers.ValidationError("width must be less than 512")
        if data['height'] < 1:
            raise serializers.ValidationError("height must be greater than 0")
        if data['height'] > 512:
            raise serializers.ValidationError("height must be less than 512")
        if data['zoom_factor'] < 1:
            raise serializers.ValidationError("zoom_factor must be greater than 0")
        if data['zoom_factor'] > 16:
            raise serializers.ValidationError("zoom_factor must be less or equal to 16")
        return data
    
class RandomColorSerializer(serializers.Serializer):
    n = serializers.IntegerField(label="N", help_text="Number of random colors to generate (1 to 10000)")
    
    def create(self, validated_data):
        return RandomColor(**validated_data)
    
    def validate(self, data):
        if data['n'] < 1:
            raise serializers.ValidationError("n must be greater than 0")
        if data['n'] > 10000:
            raise serializers.ValidationError("n must be less than 10000")
        return data