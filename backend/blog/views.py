from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse,HttpResponse

from django.views.decorators.http import require_GET

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *
import datetime
from django.utils import timezone

import socket
import sys
import os


#Usergroup(department="부서",kor_name="한글이름",eng_name="englishname",position="직책",pin="ejfoi").save()


@api_view(['GET','POST','PUT','DELETE'])
def user_detail(request,article_pk):

    if request.method == 'GET':  # 그룹의 사람들 받아오기
        article = get_object_or_404(Usergroup, pk=article_pk)
        serializer = UserDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':  # 그룹의 정보 수정
        article = Usergroup.objects.filter(id=article_pk).first()
        serializers = UserDetailSerializer(article,data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status=201)
        else:
            return  JsonResponse(serializers.data,status=400)
    elif request.method == 'DELETE':  # 그룹 내 인원 삭제
        article = Usergroup.objects.filter(id=article_pk)
        article.delete()
        return Response({'message': 'deleted successfully!'}, status=201)



@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'POST': # 그룹 내 직원 추가
        serializers = UserDetailSerializer(data=request.data)#그룹은 한글이름,영어이름,부서,직책,pin번호로 구성됨.
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=201)
        # 에러처리 하기
        else:
            return JsonResponse(serializers.data, status=400)
    elif request.method == 'GET':  # 그룹의 사람들 받아오기
        articles = Usergroup.objects.all()
        serializers = UserDetailSerializer(articles,many=True)
        return Response(serializers.data)


#출결 관리


@api_view(['GET'])#출결 1개
def access_detail_v1(request):
    article = Access.objects.all().order_by('-recent')[:10]
    serializers = AccessListSerializer(article,many=True)
    return Response(serializers.data)

@api_view(['GET','POST','PUT','DELETE'])
def access_detail_v2(request,article_pk):
    if request.method == 'POST':
        data = {'user_pk':article_pk,'enter_at':datetime.datetime.now(),'recent':datetime.datetime.now()}

        serializers = AccessListSerializer(data = data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()

            return Response(serializers.data,status=201)
        #에러처리 하기
        else :
            return JsonResponse(serializers.data,status=400)
    elif request.method == 'GET':# 출결 10개 받아오기
        article = Access.objects.filter(user_pk=article_pk).order_by('-enter_at')
        serializers = AccessListSerializer(article, many=True)
        return Response(serializers.data)
    elif request.method == 'PUT':#out_at 수정하기
        article = Access.objects.filter(user_pk=article_pk).order_by('-enter_at').first()
        #
        temp_enter = article.enter_at
        print(temp_enter)
        nowtime = datetime.datetime.now()
        data ={'enter_at':temp_enter,'out_at':nowtime,'user_pk':article_pk,'recent':nowtime}
        print(nowtime)
        serializers = AccessListSerializer(article,data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status=201)
        else :
            return  JsonResponse(serializers.data,status=400)
    elif request.method == 'DELETE':
        article = Access.objects.filter(user_pk=article_pk)
        article.delete()
        return Response({'message': 'deleted successfully!'},status=201)

@api_view(['GET'])
def camera_on(request,article_pk):
    if request.method == 'GET' :
        s = socket.socket()
        num = article_pk
        s.connect(("ssafyteam7.iptime.org", 9999))
        '''192.168.0.29'''
        s.send(bytes(str(num), 'utf8'))

        s.close()
        return Response({'message': 'camera on successfully!'}, status=201)
# Create your views here.


#get post create put update delete




