import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from HW29 import settings
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from users.models import User, Location
from users.serializers import UserSerializer, UserCreateUpdateSerializer, UserListSerializer, LocationSerializer


class UserPagination(PageNumberPagination):
    page_size = 5


class UserListView(ListAPIView):
    queryset = User.objects.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True))).order_by("username")
    serializer_class = UserListSerializer
    pagination_class = UserPagination


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocalViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
