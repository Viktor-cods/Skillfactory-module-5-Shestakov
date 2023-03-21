from django import forms
from .models import *
from django.core.exceptions import ValidationError



class PostForm(forms.ModelForm):
    postCategory = forms.ModelMultipleChoiceField(
        label='Category',
        queryset=Category.objects.all(),
    )
    postAuthor = forms.ModelChoiceField(
        label='Author',
        empty_label='Select a author',
        queryset=Author.objects.all(),
    )
    class Meta:
        model = Post
        fields = ['title','text']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 20:
            raise ValidationError({
                "text": "Описание не может быть менее 20 символов."
            })

        return cleaned_data