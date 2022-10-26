from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from articles import serializers
import articles
from articles.models import Articles
from articles.serializers import ArticlesSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class articleslist(APIView):
    def get(self, request, format=None):
        articles=Articles.objects.all()
        Serializer=ArticlesSerializer(articles, many=True)
        return Response(Serializer.data)
    @swagger_auto_schema(request_body=ArticlesSerializer)
    def post(self, request, format=None):
        Serializer = ArticlesSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(Serializer.errors)
            return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class articlestDetail(APIView):
    def get(self, request, article_id, format=None):
        article =get_object_or_404(Articles,id=article_id)
        serializers = ArticlesSerializer(article)
        return Response(serializers.data)

    def put(self, request, article_id, format=None):
        article=get_object_or_404(Articles,id=article_id)
        serializers=ArticlesSerializer(article,data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
         article =get_object_or_404(Articles,id=article_id)
         article.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)