from rest_framework import serializers
from .models import User

# define serializer which converts Users to json format for frontend to receive
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'first_name',
            'last_name',
            'email',
            'password',
            'sex'
        )
        