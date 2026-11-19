from django.core.exceptions import ValidationError

def validar_tamanho_arquivo(file):
    if file.size > 1024 * 1024: 
        raise ValidationError("A imagem deve ter no máximo 1 MB.")