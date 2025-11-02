# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

@api_view(['POST'])
def register(request):
    print("Received data:", request.data)  # << log incoming payload
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("Errors:", serializer.errors)  # << log errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
