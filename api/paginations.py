from rest_framework.pagination import PageNumberPagination, BasePagination, LimitOffsetPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 300
    page_size_query_param = 'page_size'
    max_page_size = 500

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 300