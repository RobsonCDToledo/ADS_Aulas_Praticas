# Sistema de Cadastro de Alunos e Notas

Pequeno utilitário em Python para **cadastrar alunos**, **coletar notas (0–10)**, **calcular a média** e **classificar** cada aluno como **Aprovado** ou **Reprovado** com base em um **ponto de corte** configurável.

---

## 🚀 Visão Geral

- Entrada interativa para **nomes** e **notas**.
- **Validações** de campos vazios, duplicados e intervalo das notas.
- **Encerramento** com `X` ou `SAIR`.
- **Média** por aluno e **status** (Aprovado/Reprovado) conforme `CORTE_APROVACAO` (padrão: `7.0`).
- Saída formatada com **média** em 2 casas decimais.

---

## 🔧 Como Funciona (Resumo)

1. **`notas_alunos()`**  
   Controla o fluxo de cadastro: pergunta nomes, impede duplicados/vazios, chama a coleta de notas e monta um dicionário `{aluno: [notas...]}`.

2. **`inserir_notas(mensagem=...)`**  
   Coleta várias notas por aluno, validando:

   - Não aceita vazio.
   - Converte para `float`.
   - Aceita apenas `0 ≤ nota ≤ 10`.
   - Encerra com `X`/`SAIR`.

3. **`calcular_media(lista_notas)`**  
   Retorna a média aritmética das notas; se a lista estiver vazia, retorna `0.0`.

4. **`verificar_situacao_aluno(media, ponto_corte=CORTE_APROVACAO)`**  
   Compara a média com o ponto de corte:

   - `media >= ponto_corte` → `"Aprovado"`
   - Caso contrário → `"Reprovado"`

5. **Bloco principal (`if __name__ == "__main__":`)**  
   Orquestra a execução: cadastra alunos, calcula médias, determina status e imprime o relatório final.

---

## 📌 Constante de Configuração

```python
CORTE_APROVACAO = 7.0  # altere aqui para definir outro ponto de corte
```

---

## ▶️ Execução Rápida

```bash
python seu_script.py
```

Durante a execução:

- Digite o **nome** do aluno (ou `X`/`SAIR` para encerrar).
- Informe as **notas** do aluno (ou `X`/`SAIR` para encerrar a coleta daquele aluno).
- Ao final, será exibido um resumo com **nome, notas, média e status**.

---

## ✅ Validações Implementadas

- **Nome do aluno**: não pode ser vazio; nomes duplicados são rejeitados.
- **Nota**: não pode ser vazia; deve ser numérica (`float`); deve estar entre **0** e **10**.
- **Coleta**: permite encerrar com `X`/`SAIR` tanto para nomes quanto para notas.
- **Sem notas**: alunos sem nenhuma nota válida **não** são cadastrados.

---

## 🧱 Estrutura das Funções

- `inserir_notas(mensagem)` → `list[float]`
- `calcular_media(lista_notas)` → `float`
- `verificar_situacao_aluno(media, ponto_corte)` → `str`
- `notas_alunos()` → `dict[str, list[float]]`

---

## 🖨️ Exemplo de Saída

```
Notas dos Alunos Cadastrados:
Ana, Notas: [8.0, 6.5, 7.0], Média das Notas: 7.17, Status: Aprovado
Bruno, Notas: [5.0, 6.0], Média das Notas: 5.50, Status: Reprovado
```

---

## 🔭 Próximos Passos (Ideias)

- Exportar relatório para **CSV/Excel**.
- **Ordenar** por média e exibir resumo da turma.
- Suporte a **pesos** por avaliação.
- **Internacionalização** (locale PT-BR para decimais).
- Geração de **relatório final** (aprovados, reprovados, média geral).

---

> Dúvidas ou sugestões? Abra uma **issue** ou envie um **PR**!
