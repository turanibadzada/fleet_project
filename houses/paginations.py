from rest_framework.pagination import PageNumberPagination



class HousePagination(PageNumberPagination):
    page_size = 1