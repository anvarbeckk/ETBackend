from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Question
from api.serializers import QuestionSerializer
from api.filters import QuestionFilter

class QuestionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class QuestionList(ListAPIView):
    queryset = Question.objects.order_by("?")
    serializer_class = QuestionSerializer
    pagination_class = QuestionPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = QuestionFilter
    search_fields = ['content']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"questions": serializer.data})