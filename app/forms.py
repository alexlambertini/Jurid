from django import forms
from app.models import Filme

class filmForm(forms.ModelForm):
    class Meta:
        model = Filme 
        fields = ['titulo', 'ano', 'genero', 'duracao','classificacao', 'diretor', 'imagem', 'sinopse', ]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Filme'}),
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ano de Lançamento'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gênero do Filme'}),
            'duracao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Duração do Filme'}),
            'classificacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Classificação do Filme'}),
            'diretor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diretor do Filme'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Capa do filme'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enredo do Filme'}),
        }

    
