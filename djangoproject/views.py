from time import sleep

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def slow_view(request):
    sleep(20)
    return Response('Slow View Response', status=status.HTTP_200_OK)


@api_view(['GET'])
def fast_view(request):
    return Response('Fast View Response', status=status.HTTP_200_OK)
