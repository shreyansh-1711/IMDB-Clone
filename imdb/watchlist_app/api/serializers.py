from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description']

    # Object level Validation 
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description cannot be same")
        else:
            return data
    
    
    # Feild-level Validation 
    def validate_name(self, value):
        if len(value) <2 :
            raise serializers.ValidationError("Name must be at least 2 characters")
        else:
            return value
    
    
            
        


# def name_length( value):
#     if len(value) <2 :
#         raise serializers.ValidationError("Name must be at least 2 characters")
  

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance 
    
    
#     # Object level Validation 
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description cannot be same")
#         else:
#             return data
    
    
    # Feild-level Validation 
    # def validate_name(self, value):
    #     if len(value) <2 :
    #         raise serializers.ValidationError("Name must be at least 2 characters")
    #     else:
    #         return value
    
    
            
        
    