from django.forms import forms

from books.models import book


class newbook(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
