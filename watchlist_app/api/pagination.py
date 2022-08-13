from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 4
    last_page_strings = 'end'