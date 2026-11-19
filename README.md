Ao apagar um autor que tem vários livros, os livros que correspondem aquele autor devem ser apagados juntos;

📝 Perguntas e respostas | Atividade relacionamentos - desafio


1. Que dados se perdem quando a migração é revertida? Por quê?

Resposta: Perdem-se os vínculos de coautoria. Se um livro possuía mais de um autor cadastrado no campo ManyToManyField, ao reverter para ForeignKey, o banco de dados volta a aceitar apenas um único autor por livro. O script de reversão (reverse_code) captura apenas o primeiro autor retornado, fazendo com que o vínculo com o segundo, terceiro ou demais autores daquele livro seja permanentemente apagado.

2. Com ManyToMany, o que acontece com um livro quando o seu único autor é apagado? Como garantir que todo livro tenha pelo menos um autor?

Resposta:
• O que acontece: Ao contrário da ForeignKey, que possui propriedades como on_delete=models.CASCADE, o relacionamento ManyToManyField cria uma tabela intermediária oculta. Se o único autor de um livro for deletado, a linha que ligava o autor ao livro na tabela intermediária é apagada, mas o livro continua existindo no banco de dados, tornando-se um livro "órfão" (sem nenhum autor associado).
• Como garantir que todo livro tenha pelo menos um autor: No ecossistema do Django, campos ManyToManyField não aceitam restrições de nível de banco de dados do tipo NOT NULL. Para garantir essa validação, precisamos atuar na camada da aplicação:
	1. No Admin: Sobrescrever o método clean() do formulário do admin ou do próprio modelo para lançar um erro de validação se a contagem de autores for menor que 1.
	2. No Django Signals: Utilizar o sinal m2m_changed do Django. Ele monitora a tabela intermediária e pode impedir transações ou disparar alertas caso uma remoção deixe a lista de autores vazia.





Atividade Sábado Letivo 1 -  validators, upload e CBV

1.2. Perguntas
a. O LivroModelForm mudou? Por que as regras do Model funcionam nele e no Admin sem nenhuma alteração?

Resposta: Não foi alterado. O LivroModelForm e o Admin aproveitam automaticamente os validadores definidos no Model, sem precisar de alterações.

b. Qual é a diferença entre um validator e o método clean_<campo>()? Dê um exemplo de regra que só pode ser feita com clean_<campo>().

O 'Validator' valida regras específicas, como limites numéricos, e já o campo clean_<campo> permite criar validações personalizadas para um campo.
Exemplo: Comparar o título com o nome do autor. 
 
c. Para cada regra, diga qual estratégia usar: argumento do campo, validators=[...], clean_<campo>() ou clean(). Justifique.
O título não pode ser igual ao nome do autor. --> clean_titulo()

O título deve ser salvo sem espaços no início e no fim. --> clean_titulo()
O número de páginas deve ser no máximo 5000. --> validatores=[...]
Um livro "indisponível" precisa ter o ISBN preenchido. --> clean()

Cada estratégia atende ao tipo de validação: Configuração simples, regra específica de campo ou comparação entre campo.


2.2. Perguntas
a. O que acontece se esquecermos request.FILES na view? E se esquecermos o enctype no template? Reproduza os dois erros e descreva o que viram (o formulário dá algum aviso?).

- Sem o request.FILES o django não recebe o arquivo enviado, e a capa não é salva. 
- Sem o enctype="multipart/form-data" o navegador não envia o arquivo corretamente. O django recebe os outros campos, mas não recebe a imagem. 

Nos dois casos, o formulário não apresenta aviso automático. Pode salvar o livro sem capa.

b. Qual é a diferença entre STATICFILES_DIRS / {% static %} e MEDIA_ROOT / .url? Quando usar cada um na Mini biblioteca?

STATICFILES_DIRS / {% static %} é utilizado para arquivos estáticos do projeto, como css JavaScript, ícones e imagens fixas. Enquanto o MEDIA__ROOT / url é utilizado para arquivos enviados pelos usuários, como as capas dos livros.

Utilizamos STATIC para o layout e os estilos. E o MEDIA para armazenar as capas dos livros

c. Ao excluir um livro (ou trocar a capa), o arquivo antigo continua em media/capas/. Por que isso acontece e que problema pode causar a longo prazo?

Porque o Django não exclui automaticamente os arquivos físicos quando um registro é apagado ou quando uma imagem é substituída. A longo prazo, isso pode ocupar espaço desnecessário no servidor e acumular arquivos que não são mais utilizados.


d. Por que a extensão do arquivo não basta como proteção? Que outros cuidados o servidor deve ter com uploads?