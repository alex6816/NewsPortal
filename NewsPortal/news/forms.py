from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор')
    postCategory = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категория')

    class Meta:
        model = Post
        fields = ['title', 'author', 'postCategory', 'categoryType', 'text', ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title == text:
            raise ValidationError(
                'Заголовок не должен быть идентичен тексту статьи.'
            )
        return cleaned_data

class ProfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  ]
