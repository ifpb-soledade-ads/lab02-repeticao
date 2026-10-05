# ============================================================
#  LAB 02 – Estruturas de Repetição
#  Disciplina: Laboratório de Algoritmos e Lógica de Programação
#  Curso: Análise e Desenvolvimento de Sistemas – IFPB
# ============================================================
#
#  INSTRUÇÕES:
#  - Implemente cada função conforme descrito no enunciado.
#  - NÃO altere os nomes das funções nem os parâmetros.
#  - Use laços de repetição (for / while) — NÃO use math.factorial
#    nem outras funções prontas que resolvam a questão.
#  - Nas questões 1 e 4, leia os valores com input() DENTRO da função.
#  - NÃO use break: o laço deve terminar pela sua própria condição.
#  - Após implementar, faça commit e push para o seu repositório.
#
# ============================================================


def analisar_temperaturas(qtd: int) -> str:
    """
    Lê `qtd` temperaturas com input() (podem ter casas decimais e ser
    negativas, ex.: 22.5, -3) e retorna um texto com a média, a maior
    e a menor temperatura, com duas casas decimais:
      "Média: 25.00 | Maior: 30.00 | Menor: 20.00"
    Se qtd <= 0, não lê nada e retorna "Nenhuma temperatura informada".
    """
    # TODO: implemente aqui
    pass


def calcular_fatorial(n: int) -> int:
    """
    Recebe um número inteiro n e retorna o seu fatorial (n!).
      - 0! = 1
      - n! = n * (n - 1) * ... * 1
    Caso n seja negativo, retorna -1.
    """
    # TODO: implemente aqui
    pass


def eh_primo(n: int) -> bool:
    """
    Recebe um número inteiro n e retorna True se ele for primo,
    ou False caso contrário.
    Um número é primo quando é maior que 1 e divisível apenas
    por 1 e por ele mesmo.
    """
    # TODO: implemente aqui
    pass


def simular_caixa(saldo: float) -> float:
    """
    Simula saques em um caixa eletrônico. Lê os valores de saque com
    input(), um por vez, aplicando as regras:
      - -99 → encerra a operação imediatamente.
      - valor <= 0 (diferente de -99) → saque inválido, é ignorado.
      - valor maior que o saldo atual → saldo insuficiente, é ignorado.
      - caso contrário → o valor é descontado do saldo.
    A operação também encerra quando o saldo chegar a 0.
    Se o saldo inicial já for <= 0, não lê nada e retorna o saldo.
    Retorna o saldo final.
    """
    # TODO: implemente aqui
    pass


# ============================================================
#  Use o bloco abaixo para testar suas funções no seu computador.
#  Ele NÃO é executado na correção automática.
#  Coloque chamadas de teste SOMENTE aqui dentro (indentadas):
#  chamadas fora deste bloco quebram a correção e zeram a nota.
# ============================================================
if __name__ == "__main__":
    print(analisar_temperaturas(3))
    print(calcular_fatorial(5))
    print(eh_primo(7))
    print(simular_caixa(100.0))
