import django_filters
from django_filters import CharFilter


class HikeFilter(django_filters.FilterSet):
    title = CharFilter(field_name="name", lookup_expr='icontains')


class CountyFilter(django_filters.FilterSet):
    county = CharFilter(field_name="county", lookup_expr='icontains')


class CerescopeFilter(django_filters.FilterSet):
    title = CharFilter(field_name="scientific_name", lookup_expr='icontains')
