from rest_framework import serializers
from models import bbcnews

class BbcnewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = bbcnews
        fields = ['id','title']


class BbcnewsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = bbcnews
        fields = ('id','title', 'url', 'content')