from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404,get_list_or_404
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])

def profile(request,username) : 
    person = get_object_or_404(get_user_model(),username=username)
    if request.method == "GET" :
        serializer = UserSerializer(person)
        return Response(serializer.data)
    
    elif request.method == "POST" :
        if person == request.user :
            serializer = UserSerializer(person, data={"userImg" : request.data["userImg"]}, partial=True)
            if serializer.is_valid(raise_exception=True) :
                serializer.save()
                return Response(serializer.data)
        else :
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request,user_pk) :
    if request.method == "POST" : 
        person = get_object_or_404(get_user_model(), pk = user_pk)
        user = request.user
        if person != user :
            if person.followers.filter(pk=user.pk).exists() :
                person.followers.remove(user)
                is_followed = False
            else :
                person.followers.add(user)
                is_followed = True
            
            context = {
                'is_followed' : is_followed,
                'followers_count' : person.followers.count(),
                'followings_count' : person.followings.count(),
            }
            return JsonResponse(context)

@api_view(['GET'])
def all_users(request) :
    people = get_user_model().objects.all().order_by('-point')
    serializer = UserSerializer(people, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# # @permission_classes([AllowAny])
# def signup(request):
	
#     pass
    
    
    
    
    
#     # # 1-1. Client에서 온 데이터를 받아서
#     # password = request.data.get('password')
#     # password_confirmation = request.data.get('passwordConfirmation')
		
# 	# # 1-2. 패스워드 일치 여부 체크
#     # if password != password_confirmation:
#     #     return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
# 	# # 2. UserSerializer를 통해 데이터 직렬화
#     # serializer = UserSerializer(data=request.data)
    
# 	# # 3. validation 작업 진행 -> password도 같이 직렬화 진행
#     # if serializer.is_valid(raise_exception=True):
#     #     user = serializer.save()
#     #     #4. 비밀번호 해싱 후 
#     #     user.set_password(request.data.get('password'))
#     #     user.save()
#     #     # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)

