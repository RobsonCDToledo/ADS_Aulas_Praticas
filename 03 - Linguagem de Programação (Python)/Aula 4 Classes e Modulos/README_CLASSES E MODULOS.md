# Sistema de Gerenciamento de Biblioteca

Projeto desenvolvido na Aula 4 - Bibliotecas e Modulos em Python da disciplina Linguagem de Programacao. O notebook implementa um fluxo completo para cadastrar, consultar e visualizar livros de uma biblioteca academica usando recursos padroes da linguagem e a biblioteca Matplotlib.

## Recursos Implementados

- Modelagem orientada a objetos com as classes `Livro` e `Acervo`.
- Cadastro protegido contra duplicatas com normalizacao de strings e validacao de quantidade.
- Entrada interativa para novos livros diretamente pelo usuario.
- Listagem tabular dos livros com formatacao alinhada para leitura rapida.
- Busca por titulo com retorno de todos os livros que contenham o termo informado.
- Limpeza total do acervo para reiniciar os testes do notebook.
- Importacao em lote de catlogos de exemplo para acelerar a populacao inicial.
- Visualizacao grafica da distribuicao de livros por genero utilizando Matplotlib.

## Estrutura do Notebook

1. **Contexto e objetivos**: descreve a proposta da atividade e os requisitos do sistema.
2. **Bloco de importacao**: importa `matplotlib.pyplot` e `defaultdict` da `collections`.
3. **Catalogos de teste**: define dois conjuntos de livros (`catalogo_fixo` e `catalogo_recomendacao`) para cargas automaticas ou manuais.
4. **Classes e funcoes**: implementa `Livro`, `Acervo` e os metodos de gerenciamento (`cadastrar_livro`, `cadastrar_livro_interativo`, `listar_livros`, `exibir_livros`, `buscar_por_titulo`).
5. **Carga inicial**: funcao `subir_catalogo_teste` registra os cinco livros do catalogo base no acervo.
6. **Operacoes interativas**: inclui exibicao dos livros, cadastro manual, busca por titulo e limpeza do acervo.
7. **Analise grafica**: gera grafico de barras relacionando generos e quantidades do acervo atual.

## Requisitos

- Python 3.10 ou superior.
- Ambiente capaz de executar notebooks Jupyter (JupyterLab, VS Code, Google Colab, etc.).
- Biblioteca `matplotlib` instalada (`pip install matplotlib`).

## Como Executar

1. Abra o notebook `Aula 4 - Bibliotecas E Modulos Em Python.ipynb` em seu ambiente Jupyter.
2. Execute as celulas em ordem para inicializar o acervo e carregar os catalogos de exemplo.
3. Utilize as celulas interativas para cadastrar livros adicionais, listar conteudo ou buscar por titulos especificos.
4. Rode a ultima celula para gerar o grafico de distribuicao de generos com base no estado atual do acervo.

## Possiveis Extensoes

- Persistir os dados do acervo em arquivo CSV ou banco de dados simples.
- Adicionar filtros por autor ou genero na listagem.
- Criar testes automatizados para os metodos de `Acervo`.
- Integrar uma interface grafica simples (Tkinter ou Streamlit) para o fluxo de cadastro e busca.
