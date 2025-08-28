#!/usr/bin/env py
# -*- coding: utf-8 -*-
# Autor: João pedro fidelis
# Data: 28/08/2025
"""
Arquivo python com exercicios pedidos por professor Fabiano.

Contem funções para:
- Operações matemáticas simples (par, fatorial, máximo).
- Manipulação de strings (limpeza, contagem de vogais, palíndromo).
- Processamento de vendas (total por vendedor e melhor vendedor).
"""
import re

# Questão 1
'''
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

def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par

    if n % 2 == 0: # ve se é par
        return True
    return False

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)

    if n < 0:
        raise ValueError("N não pode ser negativo...")
    if n == 0:
        return 0

    fat = 1
    while(n - 1 > 0):
        fat *= n # calcular fatorial com loop
        n -= 1 # modificar numero atual para ser ele mesmo menos 1
    return fat

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # TODO: percorra a lista guardando o maior atual

    if len(nums) == 0:
        return None

    lastNumber = None
    for num in nums: # loop entre lista de numeros
        if(lastNumber == None or num > lastNumber): # ve se numero atual é maior que anterior
            lastNumber = num # define numero atual como ultimo numero
    return lastNumber

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_

    return re.sub(r'[^\w\s]', '', s.lower()) # remove pontuações e deixa minusculo

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    # TODO: conte as vogais simples

    vogals = ['a', 'e', 'i', 'o', 'u'] # vogais
    nVog = 0
    for l in (s.lower()): # loop entre letras
        if l in vogals: # ve se letra atual é vogal
            nVog += 1
    return nVog

def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso

    inverted = ''
    ms = re.sub(r'\d+', '', s.lower()) # remove numeros e deixa minusculo
    l = len(ms)

    for n in range(l):
        inverted = inverted + ms[l-n-1] # inverte string e salva em variavel inverted
    if inverted == ms: # ve se string invertida é a mesma coisa de string normal
        return True
    return False

def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    if not vendas:
        raise ValueError("Vendas vazia...")

    totais = {}
    for nome, valor in vendas: # loop que pega nome e valor de vendas
        if nome in totais: # se nome esta ja registrado
            totais[nome] += valor # adicionar valor a mais de venda do vendedor
        else:
            totais[nome] = valor # registra vendedor na lista
    return totais

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)

    if not totais:
        raise ValueError("Totais vazio...")

    nome, total = max(totais.items(), key=lambda item: item[1]) # pega o par com o maior valor
    return nome, total