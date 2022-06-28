from django import forms
from app.models import Filme

class filmForm(forms.ModelForm):
    class Meta:
        model = Filme 
        fields = ['titulo', 'ano', 'genero',  'classificacao', 'diretor', 'sinopse', 'imagem']
  
    widgets = {
        'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        'ano': forms.NumberInput(attrs={'class': 'form-control'}),
        'diretor': forms.TextInput(attrs={'class': 'form-control'}),
        'classificacao': forms.TextInput(attrs={'class': 'form-control'}),
        'sinopse': forms.Textarea(attrs={'class': 'form-control'}),
        'imagem': forms.FileInput(attrs={'class': 'form-control'}),
    }

    
