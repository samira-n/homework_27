"""homework_27 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from ads.views.ads import AdViewSet
from ads.views.categories import CategoryViewSet
from ads.views.locations import LocationViewSet
from ads.views.service import index
from ads.views import ads as ads_view
from ads.views import users as users_view

router = routers.SimpleRouter()
router.register('ad', AdViewSet)
router.register('cat', CategoryViewSet)
router.register('location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('ad_set/', ads_view.AdListView.as_view()),
    path('user/', users_view.UserListView.as_view()),
    path('user/<int:pk>/', users_view.UserDetailView.as_view()),
    path('user/create/', users_view.UserCreateView.as_view()),
    path('user/<int:pk>/update/', users_view.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', users_view.UserDeleteView.as_view()),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
