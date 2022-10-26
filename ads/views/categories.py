import json

from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad
from ads.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
