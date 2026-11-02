# -*- coding: utf-8 -*-
"""
Criado em 02-11-2026
@author: Alef Santos Viana
Descrição: Criar um personagem RPG com nome, forca, inteligência e carismaia 
com validações de tipos e valores e formatação de saída
OBS.: Esqueci da data exata de criação do arquivo , por isso eu optei por usar a data de hoje!
"""


# Importando a função format_stat do arquivo function.py
from function import format_stat
# Função para criar um personagem RPG
# Parâmetros: nome, forca, inteligência e carismaia
# Retorna: uma string com as informações do personagem
def create_character(name,strength,intelligence,charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    elif not isinstance(strength, int):
        return "All stats should be integers"
    elif not isinstance(intelligence, int):
        return "All stats should be integers"
    elif not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    elif strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    strength = format_stat(strength)
    intelligence = format_stat(intelligence)
    charisma = format_stat(charisma)
    return f"{name}\nSTR {strength}\nINT {intelligence}\nCHA {charisma}"
# Teste da função create_character
if __name__ == '__main__':
    print(create_character('ren', 4, 2, 1))


