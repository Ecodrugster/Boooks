from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'is_read']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
