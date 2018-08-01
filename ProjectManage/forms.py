from django import forms

# from ProjectManage.models import Author, TITLE_CHOICES
#
#
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name',max_length=100)
#
#
#
# class ArticleForm(forms.Form):
#     title = forms.CharField()
#     pub_date = forms.DateField()
#
#
#
#
# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(
#         max_length=3,
#         widget=forms.Select(choices=TITLE_CHOICES),
#     )
#
#     birth_date = forms.DateField(required=False)
#
# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
from django.forms import ModelForm

from ProjectManage.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields='__all__'