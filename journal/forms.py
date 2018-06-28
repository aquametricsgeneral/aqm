from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'published_date')
        widgets = {
            'published_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
