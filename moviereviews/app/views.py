from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def home(request, format=None):
    routes_list = {
        "get_all_users": "/api/get_all_users"
    }
    if request.method == 'GET':
        return Response(routes_list)
        