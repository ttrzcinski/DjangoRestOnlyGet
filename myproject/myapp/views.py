from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SingleRoll
from .serializers import SingleRollSerializer

import random

class RollsListView(APIView):
    def get(self, request):
        # Randomize roll and save it
        randomized_roll : str = "" + (str(random.randint(1,20)))
        another_roll = SingleRoll(name={randomized_roll})
        another_roll.save()

        # Read all rolls
        rolls = SingleRoll.objects.all()
        serializer = SingleRollSerializer(rolls, many=True)
        return Response(serializer.data)
