# Explicação da Refatoração

O código original apresentava uma função com nomes curtos e pouco descritivos, além de usar loops manuais para calcular soma, média, máximo e mínimo.
A refatoração melhora a clareza e a legibilidade ao:

- dar um nome significativo à função: `summarize_numbers`
- usar um nome de parâmetro claro: `numbers`
- converter o iterável em lista apenas uma vez e verificar se não está vazio
- usar `sum()`, `max()` e `min()` para calcular os valores em vez de fazer esses cálculos manualmente
- separar a lógica de cálculo da parte de execução de exemplo usando `if __name__ == "__main__":`
- renomear as variáveis de retorno para `total`, `average`, `maximum` e `minimum`

Além disso, foi incluído um tratamento de erro para o caso de a sequência recebida estar vazia, com `ValueError`.

Essa refatoração torna o código mais fácil de entender, manter e testar.
