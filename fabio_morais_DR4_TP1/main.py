# 1 - Crie uma lista chamada ‘usuarios’ que contenha ao menos 5 listas. Cada lista interna deve representar um usuário do INFwebNET com as seguintes informações: nome (string), idade (inteiro), cidade (string) e estado (string).

usuarios = [
  ["Fabio Morais", 25, "Caruaru", "Pernambuco"],
  ["Cintia Silva", 25, "Caruaru", "Pernambuco"],
  ["Maria do Socorro", 50, "Serra Talhada", "Pernambuco"],
  ["Irineu Morais", 55, "Serra Talhada", "Pernambuco"],
  ["Mayara Morais", 29, "Caruaru", "Pernambuco"]
]

# Adicionando um usuário com dados faltando para resolver a quarta questão
usuarios.append(["Jairo Silva", 56, "", ""])

# Testando a lista usuarios
print("=============== Usuários =======================")
print(usuarios)


# 2 - Escreva um programa que leia os dados da lista ‘usuarios’ criada no exercício anterior e crie um dicionário para cada usuário. Cada dicionário deve ter as chaves "nome" e "idade" com os respectivos valores, e a chave "localização" contendo uma tupla (cidade, estado). Armazene esses dicionários em uma nova lista chamada perfis.

perfis = []

for usuario in usuarios:
  perfil = {
    "nome": usuario[0],
    "idade": usuario[1],
    "localização": (usuario[2], usuario[3])
  }
  perfis.append(perfil)

# Testando a lista perfis
print("=============== Perfis =======================")
print(perfis)


# 3 - Explique, em poucas palavras, as principais diferenças entre uma lista, um dicionário e uma tupla em Python. Dê exemplos de como cada estrutura pode ser usada no contexto da análise de dados do INFwebNET.

# Lista é uma coleção ordenada, mutável e permite itens duplicados.
# Dicionário é uma coleção ordenada, mutável e não permite item duplicado.
# Tupla é uma coleção ordenada, imutável e permite itens duplicados.

# Exemplos:
# A lista é uma boa estrutura de dados pra usuário por que permite atualização, ou seja, mutável.
# Dicionário é bom por que permite armazenar os dados completos por chave e valor, tipo: "nome": "Fábio"
# A Tupla é boa para armazenar dados fixos, como cidade e estado.

# 4 - Alguns usuários do INFwebNET forneceram informações incompletas. Remova da lista perfis todos os perfis que não possuem as informações de "nome" ou "cidade". Mantenha a lista perfis original intacta, criando uma nova lista chamada perfis_validos para armazenar os perfis válidos.

perfis_validos = [
  perfil for perfil in perfis if perfil.get("nome") and perfil["localização"][0]
]

print("=============== Perfis válidos =======================")
print(perfis_validos)