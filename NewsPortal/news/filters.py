from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from django.forms import DateInput
from .models import Post, Category

class PostFilter(FilterSet):
    date = DateFilter(field_name='dateCreation',
                    lookup_expr='gte',
                    label='Создана после',
                    widget=DateInput(attrs={'type': 'date'}))
    title = CharFilter(lookup_expr='icontains', label='Заголовок содержит')
    postCategory = ModelChoiceFilter(queryset=Category.objects.all(), label='Категория')
    date.field.error_messages = {'invalid': 'Enter date in format DD.MM.YYYY. Example: 31.12.2020'}
    date.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}


    class Meta:
        model = Post
        fields = ['title','postCategory','date',]