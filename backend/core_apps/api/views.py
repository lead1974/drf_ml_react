from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': reverse('user-register', request=request, format=format),
        # Add more endpoints here as they are created
    })
