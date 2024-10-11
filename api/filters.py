from django_filters import rest_framework as filters
from api.models import Question

class QuestionFilter(filters.FilterSet):
    level = filters.ChoiceFilter(choices=Question.LEVEL_CHOICES)
    search = filters.CharFilter(field_name="content", lookup_expr="icontains")

    class Meta:
        model = Question
        fields = ['level', 'search']


