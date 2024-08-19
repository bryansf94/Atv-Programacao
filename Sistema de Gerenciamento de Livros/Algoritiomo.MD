# Exercício: Gerenciamento de Biblioteca
Objetivo: Criar um sistema simples de gerenciamento de livros para uma biblioteca. O sistema deve permitir o cadastro de livros, consulta de livros por título e autor, e a exibição de todos os livros cadastrados.

## Parte 1: Implementação usando POO (Java ou C++)

- Classes e Objetos:
Classe Livro:
Atributos:
titulo (String)
autor (String)
anoPublicacao (int)

- Métodos:
Construtor para inicializar os atributos.
Métodos getters e setters para cada atributo.
Método exibirDetalhes() que imprime as informações do livro.
Classe Biblioteca:

- Atributos:
livros (lista ou vetor de objetos Livro)

- Métodos:
adicionarLivro(Livro livro): Adiciona um novo livro à lista.
buscarPorTitulo(String titulo): Retorna o(s) livro(s) com o título correspondente.
buscarPorAutor(String autor): Retorna o(s) livro(s) do autor correspondente.
exibirTodosLivros(): Exibe as informações de todos os livros cadastrados.

- Fluxo do Programa:
Crie uma instância da classe Biblioteca.
Adicione alguns livros à biblioteca.
Realize buscas por título e autor.
Exiba todos os livros cadastrados.

## Parte 2: Implementação sem POO (Python)

- Estruturas de Dados:
Utilize dicionários ou listas para armazenar as informações dos livros.

- Funções:
adicionar_livro(livros, titulo, autor, anoPublicacao): Adiciona um novo livro ao dicionário/lista.
buscar_por_titulo(livros, titulo): Retorna o(s) livro(s) com o título correspondente.
buscar_por_autor(livros, autor): Retorna o(s) livro(s) do autor correspondente.
exibir_todos_livros(livros): Exibe as informações de todos os livros cadastrados.

- Fluxo do Programa:
Crie uma lista ou dicionário para armazenar os livros.
Adicione alguns livros à lista ou dicionário.
Realize buscas por título e autor.
Exiba todos os livros cadastrados.

## Concluíndo:

Esse exercício permite a prática dos conceitos fundamentais de POO, como encapsulamento, criação de classes e objetos, além de mostrar a diferença na implementação de um sistema similar sem usar POO.