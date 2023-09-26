from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Vote
from .serializers import VoteSerializer
from datetime import date


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote(request):
    if request.method == 'POST':
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_results(request):
    if request.method == 'GET':
        # Get the current date
        current_date = date.today()

        # Retrieve votes for the current day
        votes = Vote.objects.filter(voted_date=current_date)

        # Serialize the votes
        serializer = VoteSerializer(votes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
