from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def options_screener(request):
    # Placeholder response for testing
    return Response({"msg": "Placeholder for options_screener endpoint"})

@api_view(['GET'])
def options_pricing(request):
    # Placeholder response for testing
    return Response({"msg": "Placeholder for options_pricing endpoint"})

@api_view(['POST'])
def options_backtest(request):
    # Placeholder response for testing
    return Response({"msg": "Placeholder for options_backtest endpoint"})
