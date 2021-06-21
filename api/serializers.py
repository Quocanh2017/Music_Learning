#convert sql to json
from rest_framework import serializers
from .models import Room

#control the output of your responses
#create a Serializer class with fields that correspond to the Model fields.
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause','votes_to_skip','created_at')

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

#create update serializer "code is unique"
class UpdateRoomSerializer(serializers.ModelSerializer):
    #set code is unique
    code = serializers.CharField(validators=[])

    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip','code')