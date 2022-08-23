from .models import Email
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import EmailSerializer, EmailListSerializer
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

# Create your views here.
#pagination for more the one results
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

#View set for accions of the API
class EmailViewSet(viewsets.GenericViewSet):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return EmailListSerializer
        return EmailSerializer

    def get_queryset(self):
        queryset = Email.objects.all()
        if self.request.GET.get('email'):
            queryset = queryset.filter(email__icontains=self.request.GET.get('email'))
        if self.request.GET.get('email_status'):
            queryset = queryset.filter(email_status=self.request.GET.get('email_status'))
        if self.request.GET.get('email_score'):
            queryset = queryset.filter(email_score=self.request.GET.get('email_score'))
        if self.request.GET.get('valid_email'):
            queryset = queryset.filter(valid_email=self.request.GET.get('valid_email'))
        if self.request.GET.get('fraud'):
            queryset = queryset.filter(fraud=self.request.GET.get('fraud'))
        else:
            queryset = queryset.order_by('-creation_date')
        return queryset
        
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
