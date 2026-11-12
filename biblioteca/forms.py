import django.forms as forms
from .models import Autor, Livro
from django.utils import timezone
from django.core.exceptions import ValidationError

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'autores',
            'ano_publicacao',
            'disponivel',
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do livro'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ano': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ano de publicação'
            }),
            'disponivel': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'categorias': forms.CheckboxSelectMultiple(),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '')

        
        titulo = ' '.join(titulo.split()) # Removendo os espaços extras

        if len(titulo) < 3:
            raise ValidationError(
                'O título precisa ter pelo menos 3 caracteres.'
            )

        return titulo

    def clean_ano(self):
        ano = self.cleaned_data.get('ano')

        ano_atual = timezone.now().year

        if ano > ano_atual:
            raise ValidationError(
                f'O ano não pode ser posterior a {ano_atual}. '
                'Informe um ano válido.'
            )

        return ano