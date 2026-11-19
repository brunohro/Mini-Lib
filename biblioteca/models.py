from django.db import models
from django.core.validators import (FileExtensionValidator, MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator)
from django.utils import timezone
from .validators import validar_tamanho_arquivo

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50) 

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.nome

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Livro(models.Model):
    capa = models.ImageField(
    upload_to='capas/',
    blank=True,
    null=True,
    validators=[
        validar_tamanho_arquivo,
        FileExtensionValidator(['jpg', 'jpeg', 'png'])
    ]
    )
    
    titulo = models.CharField(max_length=100, validators=[
        MinLengthValidator(3, 'O título precisa ter pelo menos 3 caracteres.'),
    ])

    autores = models.ManyToManyField( #ligação de muitos para muitos entre Livro e autor
        Autor, 
        related_name='livros', 
        blank=True
    )

    categoria = models.ManyToManyField(
        Category, 
        related_name='books', 
        blank=True
    )

    ano_publicacao = models.IntegerField(
        validators=[
            MinValueValidator(1450, 'O ano de publicação não pode ser anterior a 1450.'),
            MaxValueValidator(
                timezone.now().year, 
                'O ano de publicação não pode ser maior que o ano atual'
                )]
    )
    paginas = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1, message='O livro deve ter pelo menos 1 página.'),
            MaxValueValidator(5000, message='O livro não pode ter mais de 5000 páginas.')
        ]
    )

    isbn = models.CharField(
        max_length=13,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\d{13}$',
                message='O ISBN deve conter exatamente 13 dígitos.'
            )
        ]
    )

    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo