from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


from .models import Comment , Review
from . serializers import ReviewSerializer, CommentSerializer
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_create(request) :
    
    if request.method == 'GET' :
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' :
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET' :
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE' :
        review.delete()
        return Response({ 'id': review_pk}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request,review_pk) :
    
    if request.method == 'POST' :
        review = get_object_or_404(Review, pk = review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(review = review, user = request.user) # 해당 글에 댓글쓰기
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comment_list(request) :
    if request.method == 'GET' :
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request,comment_pk) :
    comment = get_object_or_404(Comment, pk = comment_pk)
    
    if request.method == 'GET' :
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    elif request.method == "DELETE" :
        comment.delete()
        data= {
            'delete' :f'댓글 {comment_pk}번이 삭제 되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT" :
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_likes(request,review_pk) :
    if request.method == "POST" :
        review = get_object_or_404(Review,pk=review_pk)
        
        if review.like_review_users.filter(pk=request.user.pk).exists():
            review.like_review_users.remove(request.user)
            review.user.point -= 10
            
            is_liked = False
        else :
            review.like_review_users.add(request.user)
            review.user.point += 10
            is_liked = True
        
        review.user.save()
        context = {
            'is_liked' : is_liked,
            'likes_count' : review.like_review_users.count()
        }
        return JsonResponse(context)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_dislikes(request,review_pk) :
    if request.method == "POST" :
        review = get_object_or_404(Review,pk=review_pk)
        
        if review.dislike_review_users.filter(pk=request.user.pk).exists():
            review.dislike_review_users.remove(request.user)
            review.user.point += 10
            is_disliked = False
        else :
            review.dislike_review_users.add(request.user)
            review.user.point -= 10
            is_disliked = True
        
        review.user.save()
        context = {
            'is_disliked' : is_disliked,
            'dislikes_count' : review.dislike_review_users.count()
        }
        return JsonResponse(context)

# @api_view(['POST'])
# def comment_create(request, review_pk) :
#     review = get_object_or_404(Review, pk = review_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True) :
#         serializer.save(review_id=review, user_id =request.user) # 해당 글에 댓글쓰기
#         return Response(serializer.data, status=status.HTTP_201_CREATED)