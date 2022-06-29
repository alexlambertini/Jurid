from django import forms
from app.models import Filme

class filmForm(forms.ModelForm):
    class Meta:
        model = Filme 
        fields = ['titulo', 'ano', 'genero', 'duracao','classificacao', 'diretor', 'imagem', 'sinopse', ]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: O Poderoso Chefão'}),
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 1972'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Ação'}),
            'duracao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2hrs'}),
            'classificacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 18'}),
            'diretor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Francis Ford Coppola'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Capa do filme'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ex: Em 1945, Don Corleone é o chefe de uma mafiosa família italiana...'}),
        }

    
