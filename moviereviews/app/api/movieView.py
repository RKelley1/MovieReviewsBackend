from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from moviereviews.app.serializers import MovieSerializer

from moviereviews.app.models import Movie

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_movie(request, format=None):
    title = request.data['title']

    movie, created = Movie.objects.get_or_create(title=title)

    if(created):
        movie.save()
        serializer = MovieSerializer(movie)
        return Response({
            'status': 201,
            'payload': serializer.data
        })
    
    else:
        raise(Exception('Movie has already been created'))