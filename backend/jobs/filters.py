import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):
    location = django_filters.CharFilter("location__name")
    category = django_filters.CharFilter("category__name")
    qualification = django_filters.CharFilter("qualification__name")
    company = django_filters.CharFilter("company__name")

    class Meta:
        model = Job
        fields = ["location", "category", "qualification", "company"]