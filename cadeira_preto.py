'''
João pedro fidelis - grupo 6

1.
a) oque é um cabeçario dentro de um arquivo python? para que serve?
    Um cabeçalho dentro de um arquivo python é uma serie de comentarios nas
    primeiras linhas do arquivo que dizem algumas informações importantes
    de serem lembradas, normalmente é separado em 5 partes tendo primeiramente
    um código de execução do script via cmd que descreve o formato especifico
    do script (python3, python, py); a segunda parte tendo o tipo de codificação
    deste arquivo (utf8 por exemplo); a terceira parte dizendo quem criou esse arquivo,
    que dia e qual versão dele; a terceira parte tendo uma breve descrição do projeto;
    e por fim como ultima parte se tem os imports padrão do python.

b) qual a diferença do cabeçario para a docstring? oque é uma docstring?
    Uma docstring é um comentario dentro de uma função que tem como objetivo especificar
    internamente como essa função funciona, sempre é o primeiro comentario de uma ou
    varias linhas dentro de uma função, e pode ser acessado utilizando a notação __doc__.

    A diferença entre um cabeçario e docstring é que um cabeçario fica no inicio do arquivo
    python e serve apenas para especificar informações estritamente do arquivo, enquanto o
    docstring é uma documentação feita sempre em inicio de funções para especificar como
    elas funcional internamente, além disso o desenvolvedor tem acesso a elas.

'''
# adicione um cabeçalho padrão neste arquivo e resolva os exercícios


def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par
    ...

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)
    ...

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # TODO: percorra a lista guardando o maior atual
    ...
import re

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...

