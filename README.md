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
