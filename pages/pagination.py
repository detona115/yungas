from rest_framework.response import Response
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            # 'links': {
            #     'next': self.get_next_link(),
            #     'previous': self.get_previous_link()
            # },
            'page': self.request.query_params.get('page', "1"),
            'page_size': self.request.query_params.get('page_size', f"{self.page_size}"),            
            'total_items': self.page.paginator.count,
            'items': data
        })