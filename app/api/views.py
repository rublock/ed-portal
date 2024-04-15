from rest_framework import generics
from mainapp import models as mainapp_models
from .serializers import NewsSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = mainapp_models.News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = mainapp_models.News.objects.all()
    serializer_class = NewsSerializer
