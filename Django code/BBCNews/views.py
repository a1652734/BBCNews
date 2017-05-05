from django.shortcuts import render
from rest_framework import generics
from serializers import BbcnewsSerializer, BbcnewsDetailSerializer
from models import bbcnews

class BBCNewsList(generics.ListCreateAPIView):
	queryset = bbcnews.objects.all()
	serializer_class = BbcnewsSerializer

class BBCNewsDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = bbcnews.objects.all()
	serializer_class = BbcnewsDetailSerializer


	
		