from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
from django.core.cache import cache

from IPython import embed
# Create your views here.
@api_view(['GET'])
def music_list(request):


    # musics = cache.get('musics', None)
    # if not musics:
    #     musics = Music.objects.all()
    #     cache.set('musics', musics, 10)

    musics = Music.objects.all()
    # # embed()
    # for i in range(10000):
    #     print(i%5)
    #     Music.objects.create(artist=Artist.objects.get(id=(i%5+1)), title="곡번호"+str(i))
    serializer=MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)


@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, id=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, music_pk):
    # request.data는 사용자가 HTTP body에 담아 날린 댓글(content) 내용
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response(serializer.data)
    
@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated!!'})
    # DELETE
    else:
        comment.delete()
        return Response({'message': 'Comment has been deleted!!'})

