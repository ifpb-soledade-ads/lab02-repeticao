# Lab 02 – Estruturas de Repetição

**Disciplina:** Laboratório de Algoritmos e Lógica de Programação  
**Curso:** Análise e Desenvolvimento de Sistemas – IFPB  
**Pontuação total:** 100 pontos  

---

## Objetivo

Praticar o uso de estruturas de repetição (`for` e `while`) em Python,
incluindo acumuladores, contadores e **condições de parada bem escritas**.

---

## Como entregar

1. Aceite o laboratório com `gh student accept ifpb-soledade-ads lalp-2026-2 lab02-repeticao`
   (ou pelo link disponibilizado pelo professor).
2. Clone o repositório gerado para você e entre na pasta.
3. Edite **apenas** o arquivo `src/solucao.py`.
4. Envie sua solução com `gh student submit` (ou `git add`, `git commit` e `git push`).
5. Após o envio, acesse as abas **Actions** e **Releases** do seu repositório para ver o
   resultado da correção automática.

>  **Não modifique** nenhum outro arquivo do repositório.

> Resolva as questões **usando laços de repetição**. Não use `math.factorial`
> nem outras funções prontas que resolvam a questão por você.

> **Não use `break`.** O laço deve terminar pela própria condição do `while`
> (ou pelo fim do `for`).

> **Para testar no seu computador**, rode `python src/solucao.py` e coloque as
> chamadas das funções **somente** dentro do bloco `if __name__ == "__main__":`
> que já está no fim do arquivo. Chamadas (ou `input()`) fora desse bloco quebram
> a correção automática e **zeram a nota do laboratório inteiro**.

---

## Questões

### Q1 – Análise de Temperaturas `(25 pontos)`

Implemente a função `analisar_temperaturas(qtd: int) -> str` que recebe a
quantidade de medições do dia, **lê cada temperatura com `input()`** dentro de
um laço `for` e retorna um texto com a **média**, a **maior** e a **menor**
temperatura lidas, no formato:

```
Média: 25.00 | Maior: 30.00 | Menor: 20.00
```

- Todos os valores com **duas casas decimais** (dica: `f"{valor:.2f}"`).
- As temperaturas podem ter **casas decimais** (ex.: `22.5`) e podem ser
  **negativas** (ex.: `-3`) — converta com `float()`, não `int()`.
- A função deve ler **exatamente** `qtd` temperaturas.
- Se `qtd <= 0`, não lê nada e retorna `"Nenhuma temperatura informada"`.

Exemplo: com `qtd = 3` e as temperaturas `20`, `25` e `30` digitadas, o retorno é
`"Média: 25.00 | Maior: 30.00 | Menor: 20.00"`.

> Pense bem em qual valor inicial dar para as variáveis do maior e do menor:
> ele precisa funcionar para **quaisquer** temperaturas, inclusive negativas.

---

### Q2 – Fatorial `(25 pontos)`

Implemente `calcular_fatorial(n: int) -> int` que retorna o fatorial de `n`:

| Entrada      | Retorno                        |
|--------------|--------------------------------|
| `n == 0`     | `1`                            |
| `n > 0`      | `n * (n - 1) * (n - 2) * ... * 1` |
| `n < 0`      | `-1` (entrada inválida)        |

Exemplo: `calcular_fatorial(5)` → `120` (5 × 4 × 3 × 2 × 1)

---

### Q3 – Número Primo `(25 pontos)`

Implemente `eh_primo(n: int) -> bool` que retorna `True` se `n` for primo e
`False` caso contrário.

- Um número é **primo** quando é **maior que 1** e divisível apenas por 1 e
  por ele mesmo.
- `0`, `1` e números negativos **não** são primos.

Exemplos: `eh_primo(7)` → `True` · `eh_primo(9)` → `False` · `eh_primo(2)` → `True`

---

### Q4 – Caixa Eletrônico `(25 pontos)`

Implemente `simular_caixa(saldo: float) -> float` que recebe o saldo inicial da
conta, **lê os valores de saque com `input()`** dentro de um laço e retorna o
**saldo final**.

A cada valor lido, aplique as regras:

| Valor do saque                     | Ação                                        |
|------------------------------------|---------------------------------------------|
| `-99`                              | Encerra a operação imediatamente            |
| `<= 0` (diferente de `-99`)        | Saque inválido → ignora e lê o próximo      |
| maior que o saldo atual            | Saldo insuficiente → ignora e lê o próximo  |
| caso contrário                     | Desconta o valor do saldo                   |

- A operação também **encerra** quando o saldo chegar a `0` (sem ler mais nada).
- Se o saldo inicial já for `<= 0`, a função **não lê nada** e retorna o próprio saldo.
- Não use `break`: as duas formas de encerrar (`-99` e saldo zerado) devem estar
  na **condição do `while`**.

Exemplo: com `saldo = 100.0` e os valores `30`, `-10`, `200`, `50`, `-99` digitados:

```
100 - 30 = 70 → -10 inválido → 200 insuficiente → 70 - 50 = 20 → -99 encerra
```

O retorno é `20.0`.

---

## Critérios de avaliação

Cada questão é avaliada por testes automatizados que rodam após o seu envio
(você não tem acesso a eles diretamente). A nota é proporcional ao número de
testes que passam dentro de cada questão (25 pts cada).

Além da correção automática, o professor pode revisar o código fonte para
verificar boas práticas e o uso correto das estruturas de repetição.

---

*Bons estudos!* 
