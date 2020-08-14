from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from moviereviews.app.serializers import CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from moviereviews.app.models import Comment, Movie


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, format=None):
    userID = int(request.data['userID'])
    movieID = int(request.data['movieID'])
    content = request.data['content']
    upvotes = int(request.data['upvotes'])
    user = get_object_or_404(User, pk=userID)
    movie = get_object_or_404(Movie, pk=movieID)
    try:
        comment = Comment.objects.create(movie=movie, user=user, content=content, upvotes=upvotes)
        serializer = CommentSerializer(comment, many=False)
        return Response({
            'status': 201,
            'payload': serializer.data
        })
    except Exception as e:
        raise(e)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments_for_movie(request, format=None):
    movieID = int(request.GET.get('movie_id', None))
    comments = get_list_or_404(Comment, movie_id=movieID)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments_for_user(request, format=None):
    userID = int(request.GET.get('user_id', None))
    comments = get_list_or_404(Comment, user_id=userID)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_upvote_count(request, format=None):
    commentID = int(request.data['commentID'])
    update = request.data['update']
    comment = get_object_or_404(Comment, pk=commentID)
    serializer = CommentSerializer(comment, many=False)
    if update == 'INCREMENT':
        comment.upvotes += 1
        comment.save()
        return Response(serializer.data)
    if update == 'DECREMENT':
        comment.upvotes -= 1
        comment.save()
        return Response(serializer.data)