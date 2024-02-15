from django.shortcuts import render

# Create your views here.
from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework import permissions, status, generics, viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework import mixins
from .serializers import JobSerializer, LocationSerializer, CompanySerializer, QualificationSerializer, CategorySerializer
from .models import Job, Location, Company, Qualification, Category
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .filters import JobFilter
import django_filters
from drf_multiple_model.views import ObjectMultipleModelAPIView


class JobViewSet(AutoPrefetchViewSetMixin, mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):

    queryset = Job.objects.all()
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )
    filter_class = JobFilter
    search_fields = ['id', 'description', 'location__name',
                     "category__name", "qualification__name", "company__name", "title"]
    ordering_fields = "__all__"
    # ordering = ['title']

    permission_classes_by_action = {
        'perform_update': [permissions.IsAuthenticated],
        'list': [permissions.AllowAny],
        'retrieve': [permissions.AllowAny]
    }

    serializer_class = JobSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        if(self.request.user in instance.applicants.all()):
            instance.applicants.remove(self.request.user)
        else:
            instance.applicants.add(self.request.user)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    # @method_decorator(cache_page(60*15))
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)


class FilterAPIView(ObjectMultipleModelAPIView):
    permission_classes = (permissions.AllowAny,)

    querylist = [
        {'queryset': Location.objects.all(
        ), 'serializer_class': LocationSerializer},
        {'queryset': Category.objects.all(
        ), 'serializer_class': CategorySerializer},
        {'queryset': Qualification.objects.all(
        ), 'serializer_class': QualificationSerializer},
        {'queryset': Company.objects.all(
        ), 'serializer_class': CompanySerializer},
    ]