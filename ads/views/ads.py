import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView
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

        return super().get(request, *args, **kwargs)

# class AdListView(ListView):
#     model = Ad
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         self.object_list = self.object_list.order_by("-price")
#
#         paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#
#         return JsonResponse(
#             {
#                 "items": [
#                     {
#                         "id": ad.id,
#                         "name": ad.name,
#                         "author_id": ad.author_id,
#                         "author": ad.author.username,
#                         "price": ad.price,
#                         "description": ad.description,
#                         "is_published": ad.is_published,
#                         "category_id": ad.category_id,
#                         "image": ad.image.url if ad.image else None
#                     }
#                     for ad in page_obj
#                 ],
#                 "num_pages": page_obj.paginator.num_pages,
#                 "total": page_obj.paginator.count
#             }
#         )
#
#
# class AdDetailView(DetailView):
#     model = Ad
#
#     def get(self, request, *args, **kwargs):
#         ad = self.get_object()
#
#         return JsonResponse({
#             "id": ad.id,
#             "name": ad.name,
#             "author_id": ad.author_id,
#             "author": ad.author.username,
#             "price": ad.price,
#             "description": ad.description,
#             "is_published": ad.is_published,
#             "category_id": ad.category_id,
#             "image": ad.image.url if ad.image else None
#         })
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AdCreateView(CreateView):
#     model = Ad
#     fields = ['name', 'author', 'price', 'description', 'is_published', 'category']
#
#     def post(self, request, *args, **kwargs):
#         ad_data = json.loads(request.body)
#
#         ad = Ad.objects.create(
#             name=ad_data['name'],
#             author=get_object_or_404(User, pk=ad_data['author_id']),
#             price=ad_data['price'],
#             description=ad_data['description'],
#             is_published=ad_data['is_published'],
#             category=get_object_or_404(Category, pk=ad_data['category_id']),
#         )
#
#         return JsonResponse({
#             "id": ad.id,
#             "name": ad.name,
#             "author_id": ad.author_id,
#             "author": ad.author.username,
#             "price": ad.price,
#             "description": ad.description,
#             "is_published": ad.is_published,
#             "category_id": ad.category_id,
#             "image": ad.image.url if ad.image else None
#         })
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AdUpdateView(UpdateView):
#     model = Ad
#     fields = ['name', 'author', 'price', 'description', 'is_published', 'category']
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#
#         ad_data = json.loads(request.body)
#         self.object.name = ad_data['name']
#         self.object.price = ad_data['price']
#         self.object.description = ad_data['description']
#         self.object.author = get_object_or_404(User, pk=ad_data['author_id'])
#         self.object.category = get_object_or_404(Category, pk=ad_data['category_id'])
#
#         self.object.save()
#
#         return JsonResponse({
#             "id": self.object.id,
#             "name": self.object.name,
#             "author_id": self.object.author_id,
#             "author": self.object.author.username,
#             "price": self.object.price,
#             "description": self.object.description,
#             "is_published": self.object.is_published,
#             "category_id": self.object.category_id,
#             "image": self.object.image.url if self.object.image else None
#         })
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class AdDeleteView(DeleteView):
#     model = Ad
#     success_url = "/"
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({"status": "ok"}, status=200)
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class AdUploadImageView(UpdateView):
#     model = Ad
#     fields = ['image']
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#
#         self.object.image = request.FILES.get('image', None)
#         self.object.save()
#
#         return JsonResponse({
#             "id": self.object.id,
#             "name": self.object.name,
#             "author_id": self.object.author_id,
#             "author": self.object.author.username,
#             "price": self.object.price,
#             "description": self.object.description,
#             "is_published": self.object.is_published,
#             "category_id": self.object.category_id,
#             "image": self.object.image.url if self.object.image else None
#         })
