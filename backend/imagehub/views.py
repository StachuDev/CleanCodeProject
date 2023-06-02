from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

from .models import *
from .models import Account
from .serializers import *   



# --- tag --- 

@api_view(['GET', 'POST'])
def tag_list(request):
    if request.method == 'GET':
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def tag_detail(request, pk, format=None):

    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TagSerializer(instance=tag, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = TagSerializer(instance=tag, data=request.data, partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# --- post ---

@api_view(['GET', 'POST'])
# @parser_classes([MultiPartParser, FormParser])
def post_list(request):
    user = request.user.id
    data = request.data

    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        try:
            tag = Tag.objects.get(tag=request.data['tag'])
        except:
            Tag.objects.create(tag=request.data['tag'])

        data = data.copy()
        data['user'] = user

        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    serializer = FullPostSerializer(post)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
# @parser_classes([MultiPartParser, FormParser])
def edit_post(request, pk, format=None):
    user = request.user.id

    try:
        post = Post.objects.get(pk=pk, user=user)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
  
    elif request.method == 'PUT':
        try:
            tag = Tag.objects.get(tag=request.data['tag'])
        except:
            Tag.objects.create(tag=request.data['tag'])

        serializer = PostSerializer(post, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        if request.data.get('tag') is not None:
            try:
                tag = Tag.objects.get(tag=request.data['tag'])
            except:
                Tag.objects.create(tag=request.data['tag'])
        
            serializer = PostSerializer(post, data=request.data, partial=True)
        else:
            serializer = PostNoTagSerializer(post, data=request.data, partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# --- comment ---

@api_view(['GET'])
def comment_list(request):
    post = request.data.get('post')
    
    comment = Comment.objects.filter(post=post)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)


@api_view(['POST'])    
@permission_classes([IsAuthenticated])
def add_comment(request):
    user = request.user.id
    data = request.data

    data = data.copy()
    data['user'] = user

    serializer = CommentSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, pk, format=None):
    user = request.user.id
    post = request.data.get('post')

    try:
        comment = Comment.objects.get(pk=pk, post=post, user=user)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
  
    elif request.method == 'PATCH':
        serializer = CommentSerializer(instance=comment, data=request.data, partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# --- subcomment ---

@api_view(['GET'])
def subcomment_list(request):
    parrent_comment = request.data.get('comment')

    subcomment = Subcomment.objects.filter(parrent_comment=parrent_comment)
    serializer = SubcommentSerializer(subcomment, many=True)
    return Response(serializer.data)


@api_view(['POST'])    
@permission_classes([IsAuthenticated])
def add_subcomment(request):
    user = request.user.id
    data = request.data
    
    data = data.copy()
    data['user'] = user

    serializer = SubcommentSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def subcomment_detail(request, pk, format=None):
    user = request.user.id
    parrent_comment = request.data.get('comment')

    try:
        subcomment = Subcomment.objects.get(pk=pk, parrent_comment=parrent_comment, user=user)
    except Subcomment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = SubcommentSerializer(subcomment)
        return Response(serializer.data)
  
    elif request.method == 'PATCH':
        serializer = SubcommentSerializer(instance=subcomment, data=request.data, partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        subcomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# --- post likes

@api_view(['GET'])
def postlike_list(request):
    post = request.data.get('post')

    postlike = PostLike.objects.filter(post=post)
    serializer = PostLikeSerializer(postlike, many=True)
    return Response(serializer.data)


@api_view(['POST'])    
@permission_classes([IsAuthenticated])
def add_postlike(request):
    user = request.user.id
    post = request.data.get('post')
    data = request.data

    try:
        like = PostLike.objects.get(user=user, post=post)
    except:
        like = None

    if like is not None:
        return Response(status=status.HTTP_208_ALREADY_REPORTED)

    post_obj = Post.objects.get(id=post)

    
    data = data.copy()
    like_type = request.data.get('type')
    # return Response(like_type)
    if like_type == "1": 
        post_obj.like_count = post_obj.like_count + 1
        post_obj.save()
    elif like_type == "0": 
        post_obj.dislike_count = post_obj.dislike_count + 1
        post_obj.save()

    data['user'] = user

    serializer = PostLikeSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def postlike_detail(request, pk, format=None):
    user = request.user.id
    post = request.data.get('post')

    try:
        postlike = PostLike.objects.get(pk=pk, post=post, user=user)
    except PostLike.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = PostLikeSerializer(postlike)
        return Response(serializer.data)
  
    elif request.method == 'PATCH':
        serializer = PostLikeSerializer(instance=postlike, data=request.data, partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        postlike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
