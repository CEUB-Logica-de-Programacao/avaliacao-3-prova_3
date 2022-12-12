# ## Desafio
#
# Dados ``n`` pares de parênteses, escreva uma função para gerar todas as combinações de parênteses bem formados.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# n = 3
# ```
#
# A saída deve ser:
#
# ```
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# ```
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def bonus(n):
    def printParenteses(str, n):
    if(n > 0):
        _printParenteses(str, 0,
                          n, 0, 0)
    return
def _printParenteses(str, pos, n,
                      open, close):
    if(close == n):
        for i in str:
            print(i, end="")
        print()
        return
    else:
        if(open > close):
            str[pos] = ')'
            _printParenteses(str, pos + 1, n,
                              open, close + 1)
        if(open < n):
            str[pos] = '('
            _printParenteses(str, pos + 1, n,
                              open + 1, close)                            
str = [""] * 2 * n
printParenteses(str, n)
if __name__ == '__main__':
    print(bonus(10))
