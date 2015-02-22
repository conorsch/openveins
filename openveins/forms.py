from django import forms
from openveins.models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'source', 'year', 'editorial']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'e.g. Voltaire'}),
            'text': forms.Textarea(attrs={'placeholder': 'In the beginning...'}),
            'editorial': forms.Textarea(attrs={'placeholder': 'e.g. lol'}),
        }
