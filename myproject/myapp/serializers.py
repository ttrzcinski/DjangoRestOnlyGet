from rest_framework import serializers
from .models import SingleRoll

class SingleRollSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleRoll
        fields = '__all__'
