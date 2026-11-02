# Projeto Personagem RPG

Projeto de criação de personagens de RPG em Python, com validação de atributos e
visualização em "pontos" (dots), executado no terminal.

- **Autor:** Alef Santos Viana
- **Versão:** 1.0
- **Data:** 02-11-2026

## Descrição

Aplicação que monta um personagem de RPG a partir de um **nome** e de três
atributos — **força** (`STR`), **inteligência** (`INT`) e **carisma** (`CHA`).
Os dados são validados quanto ao tipo e aos valores permitidos antes de serem
formatados para exibição.

## Regras de negócio

### Nome

- Deve ser uma string.
- Não pode ser vazio.
- Não pode ter mais de **10 caracteres**.
- Não pode conter espaços.

### Atributos (força, inteligência, carisma)

- Devem ser números inteiros.
- Cada atributo deve estar entre **1 e 4**.
- A soma dos três atributos deve ser exatamente **7**.

### Visualização (dots)

Cada atributo é exibido como uma barra de **10 espaços**:

- `●` (ponto cheio) representa cada ponto do atributo.
- `○` (ponto vazio) representa os espaços restantes.

Exemplo: um atributo de valor `4` é exibido como `●●●●○○○○○○`.

## Estrutura do projeto

```
personagem_RPG/
├── personagem_Rpg.py   # Função create_character e validações
├── function.py         # Função format_stat (formatação em dots)
└── README.md
```

- **`personagem_Rpg.py`** — define `create_character(name, strength, intelligence, charisma)`,
  responsável por validar os dados e montar a saída do personagem.
- **`function.py`** — define `format_stat(value)`, que converte um valor inteiro
  na barra de 10 dots, além das constantes `full_dot` (`●`) e `empty_dot` (`○`).

## Requisitos

- Python 3.x

Não há dependências externas — o projeto usa apenas a biblioteca padrão do Python.

## Como executar

Execute o programa a partir da pasta do projeto (necessário para o import de
`function.py` funcionar):

```bash
cd personagem_RPG
python3 personagem_Rpg.py
```

O arquivo `personagem_Rpg.py` traz um exemplo de uso na seção `__main__`:

```python
print(create_character('ren', 4, 2, 1))
```

## Exemplo de uso

```python
from personagem_Rpg import create_character

print(create_character('ren', 4, 2, 1))
```

Saída:

```
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

Em caso de dados inválidos, a função retorna uma mensagem de erro, por exemplo:

```
The character should start with 7 points
```

## Possíveis melhorias futuras

- Aceitar nomes com espaços e ampliar o limite de caracteres.
- Parametrizar o total de pontos (hoje fixo em 7) e o tamanho da barra de dots (10).
- Persistir os personagens criados em arquivo (JSON/CSV).
- Criar testes automatizados para as validações.
