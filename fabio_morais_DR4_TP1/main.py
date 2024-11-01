# 1 - Crie uma lista chamada ‘usuarios’ que contenha ao menos 5 listas. Cada lista interna deve representar um usuário do INFwebNET com as seguintes informações: nome (string), idade (inteiro), cidade (string) e estado (string).

usuarios = [
  ["Fabio Morais", 25, "Caruaru", "Pernambuco"],
  ["Cintia Silva", 25, "Caruaru", "Pernambuco"],
  ["Maria do Socorro", 50, "Serra Talhada", "Pernambuco"],
  ["Irineu Morais", 55, "Serra Talhada", "Pernambuco"],
  ["Mayara Morais", 29, "Caruaru", "Pernambuco"]
]

# 2 - Escreva um programa que leia os dados da lista ‘usuarios’ criada no exercício anterior e crie um dicionário para cada usuário. Cada dicionário deve ter as chaves "nome" e "idade" com os respectivos valores, e a chave "localização" contendo uma tupla (cidade, estado). Armazene esses dicionários em uma nova lista chamada perfis.

perfis = []

for usuario in usuarios:
  perfil = {
    "nome": usuario[0],
    "idade": usuario[1],
    "localização": (usuario[2], usuario[3])
  }
  perfis.append(perfil)
