from rest_framework.decorators import api_view
from rest_framework.response import Response
from moviereviews.app.models import User


@api_view(['POST'])
def generate_token(request, format=None):
    pass
