import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad, User
from ads.serializers import AdSerializer
from homework_27 import settings


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat', [])
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        ad_text = request.GET.get('name')
        if ad_text:
            self.queryset = self.queryset.filter(name__icontains=ad_text)

        location_text = request.GET.get('location')
        if location_text:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location_text)

        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=int(price_from))
        if price_to:
            self.queryset = self.queryset.filter(price__lte=int(price_to))

        return super().get(request, *args, **kwargs)
