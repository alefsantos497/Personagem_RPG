# -*- coding: utf-8 -*-
"""
Criado em 02-11-2026
@author: Alef Santos Viana
Descrição: Função para formatar os valores de estatísticas de um personagem RPG
"""
# Variáveis globais para representar os pontos cheios e vazios
# Usadas na formatação dos valores de estatísticas
# OBS.: Esqueci da data exata de criação do arquivo , por isso eu optei por usar a data de hoje!
full_dot = '●'
empty_dot = '○' 
def format_stat(value):
    return full_dot * value + empty_dot * (10 - value)
if __name__ == '__main__':
    print(format_stat(4))