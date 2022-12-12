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
    def gerarParenteses(n,  Open,  close,  s, ans):
 
    if(Open == n and close == n):
        ans.append(s)
        return
 

    if(Open < n):
        gerarParenteses(n, Open+1, close, s+"{", ans)
 
  
    if(close < Open):
        gerarParenteses(n, Open, close + 1, s+"}", ans)
 
 
n = 3
 

ans = []
 
gerarParenteses(n, 0, 0, "", ans)
 
for s in ans:
    print(s)
if __name__ == '__main__':
    print(bonus(10))
