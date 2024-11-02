import random
from collections import Counter

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
print("")
print("=============== Usuários =======================")
print(usuarios)
print("")


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
print("")
print("=============== Perfis =======================")
print(perfis)
print("")


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

print("")
print("=============== Perfis válidos =======================")
print(perfis_validos)
print("")

# 5 - Crie uma implementação que leia os dados presentes no arquivo "base_inicial.txt" e os armazene na lista perfis_validos, criando novas palavras-chave para os dados adicionais encontrados. (O arquivo está disponível no repositório.)

# Links usados como reforço: https://awari.com.br/python-a-leitura-de-arquivos-txt/ | https://awari.com.br/arquivo-txt-python-aprenda-a-ler-e-manipular-arquivos-de-texto-com-python/

# Quando fui testar a 6° questão estava dando erro de diretorio ([Errno 2] No such file or directory: 'base_inicial.txt'), só consegui quando coloquei o diretorio completo.
with open(r"C:\python-infnet\python-dados-4t24\repositorio-python-para-dados-4t24-prof-dacio-souza-fabiolmorais\fabio_morais_DR4_TP1\base_inicial.txt", "r", encoding="utf-8") as base_inicial:
  leitor = base_inicial.readlines()[1:]

  for linha in leitor:
    dados = linha.strip().split('?')

    # Modificando o código para definir um padrão para lidar com dados ausentes

    nome = dados[0] if dados[0] else None
    idade = int(dados[1]) if dados[1].isdigit() else None
    cidade = dados[2] if dados[2] else None
    estado = dados[3] if dados[3] else None
    amigos = dados[4:] if len(dados) > 4 else []

    if nome and cidade:
      perfil = {
        "nome": nome,
        "idade": idade,
        "localização": (cidade, estado),
        "amigos": amigos
      }
      perfis_validos.append(perfil)

print("")
print("=============== Perfis válidos após 4° questão =======================")
print(perfis_validos)
print("")

# 6 - Com os dados carregados no exercício anterior, adicione os usuários dos exercícios 1 e 2, definindo um padrão para lidar com os dados ausentes e salve estas informações em um arquivo "rede_INFNET.txt".

for perfil in perfis:
  perfil['amigos'] = []

print("")
print("=============== Perfis 6° questão =======================")
print(perfis)
print("")

perfis_validos.extend(perfis)

print("")
print("=============== Perfis válidos 6° questão =======================")
print(perfis_validos)
print("")

# with open("rede_INFNET.txt", "w", encoding="UTF-8") as rede_INFNET:
#   for perfil in perfis_validos:
#     escritor = (
#       f"Nome: {perfil['nome']}, "
#       f"Idade: {perfil['idade']}, "
#       f"Localização: {perfil['localização'][0]}, {perfil['localização'][1]}, "
#       f"Amigos: {', '.join(perfil['amigos']) if perfil['amigos'] else 'Nenhum'}\n"
#     )
#     rede_INFNET.write(escritor)

print("")
print("Dados salvos com sucesso!!!")
print("")

# 7 - Com o dicionário criado no exercício anterior, adicione um novo amigo ao set de amigos de um usuário específico.

for perfil in perfis_validos:
  if perfil["nome"] == "Fabio Morais":
    if not isinstance(perfil["amigos"], set):
      perfil["amigos"] = set(perfil["amigos"])

    perfil["amigos"].add("Vini")
    break

print("")
print("=============== Perfis válidos 7° questão =======================")
print(perfis_validos)
print("")

# 8 - Crie um programa que permita verificar se um determinado usuário foi adicionado como amigo de mais de 4 usuários. Caso tenha, exiba uma mensagem afirmando que o usuário é "popular".

amigo_popular = {}

for perfil in perfis_validos:
  amigos = perfil.get("amigos", set())
  for amigo in amigos:
    if amigo in amigo_popular:
      amigo_popular[amigo] += 1
    else:
      amigo_popular[amigo] = 1

for amigo, contagem in amigo_popular.items():
  if contagem > 4:
    print(f"{amigo} é popular!")


# 9 - Crie um programa que selecione dois perfis aleatórios e utilize sets para armazenar os amigos de cada um desses usuários do INFwebNET. Exiba os amigos em comum entre esses dois usuários, utilizando métodos e operação de sets.

usuario1, usuario2 = random.sample(perfis_validos, 2)

amigos_usuario1 = set(usuario1.get("amigos", []))
amigos_usuario2 = set(usuario2.get("amigos", []))

amigos_em_comum = amigos_usuario1.intersection(amigos_usuario2)

print("")
print("=============== Amigos em comum =======================")
print(f"Amigos em comum entre {usuario1['nome']} e {usuario2['nome']}: {amigos_em_comum if amigos_em_comum else 'Não tem amigos em comum'}")
print("")

# 10 - Utilizando os sets do exercício anterior, exiba os amigos que são exclusivos de cada usuário, ou seja, aqueles que não são amigos em comum.

amigos_exclusivos_usuario1 = amigos_usuario1 - amigos_em_comum
amigos_exclusivos_usuario2 = amigos_usuario2 - amigos_em_comum

print("")
print("=============== Amigos exclusivos =======================")
print(f"Amigos exclusivos de {usuario1['nome']}: {amigos_exclusivos_usuario1 if amigos_exclusivos_usuario1 else 'Não tem amigos exclusivos'}")
print(f"Amigos exclusivos de {usuario2['nome']}: {amigos_exclusivos_usuario2 if amigos_exclusivos_usuario2 else 'Não tem amigos exclusivos'}")
print("")

# 11 - Permita que o usuário remova um amigo da lista de conexões de um membro do INFwebNET específico no dicionário criado no exercício 4.

# nome_usuario = input("Digite o nome do usuário: ")
# nome_amigo = input("Digite o nome do amigo: ")

# usuario_encontrado = None
# for perfil in perfis_validos:
#   if perfil["nome"] == nome_usuario:
#     usuario_encontrado = perfil
#     break

# if usuario_encontrado:
#   if nome_amigo in usuario_encontrado["amigos"]:
#     usuario_encontrado["amigos"].remove(nome_amigo)
#     print(f"Amigo {nome_amigo} removido de {nome_usuario}")
#   else:
#     print(f"{nome_amigo} não está na lista de amigos de {nome_usuario}!")
# else:
#   print(f"Usuário {nome_usuario} não encontrado!")

# 12 - Após adicionar ou remover amigos, salve o dicionário atualizado em um novo arquivo chamado "rede_INFNET_atualizado.txt".

# with open("rede_INFNET_atualizado.txt", "w", encoding="UTF-8") as rede_INFNET_atualizado:
#   for perfil in perfis_validos:
#     escritor = (
#       f"Nome: {perfil['nome']}, "
#       f"Idade: {perfil['idade']}, "
#       f"Localização: {perfil['localização'][0]}, {perfil['localização'][1]}, "
#       f"Amigos: {', '.join(perfil['amigos']) if perfil['amigos'] else 'Nenhum'}\n"
#     )
#     rede_INFNET_atualizado.write(escritor)

# print("")
# print("Dados salvos com sucesso!!!")
# print("")

# 13 - Escreva um programa que leia o arquivo "rede_INFNET.txt" e imprima na tela a lista dos nomes de todos os usuários da rede social.

nomes = []
with open(r"C:\python-infnet\python-dados-4t24\repositorio-python-para-dados-4t24-prof-dacio-souza-fabiolmorais\rede_INFNET.txt", "r", encoding="utf-8") as rede_INFNET:

  for linha in rede_INFNET:
    if "Nome:" in linha:
      dados = linha.split(",")
      for dado in dados:
        if dado.startswith("Nome:"):
          nomes.append(dado.split("Nome: ")[1].strip())
          break

print("")
print("=============== Usuários INFwebNET =======================")
print(nomes)
print("")

# 14 - Crie uma função que leia o arquivo "rede_INFNET.txt" e mostre quantos amigos cada usuário possui, imprimindo o nome do usuário e a quantidade de amigos.


def total_amigos(lista):
  usuarios = []

  with open(lista, "r", encoding="utf-8") as rede_INFNET:
    leitor = rede_INFNET.readlines()
    for linha in leitor:
      dados = linha.strip().split(", ")

      nome = dados[0].split(": ")[1]
      idade = int(dados[1].split(": ")[1])
      cidade = dados[2].split(": ")[1]
      estado = dados[3]
      amigos = dados[4:]

      if "Amigos: Nenhum" in amigos:
        amigos = []

      usuario = {
        "Nome": nome,
        "Idade": idade,
        "Localização": (cidade, estado),
        "Amigos": amigos
      }
      usuarios.append(usuario)

  for usuario in usuarios:
    nome = usuario["Nome"]
    quantidade_amigos = len(usuario["Amigos"])
    print(f"{nome}: {quantidade_amigos} amigo(s).")


# total_amigos(r"C:\python-infnet\python-dados-4t24\repositorio-python-para-dados-4t24-prof-dacio-souza-fabiolmorais\rede_INFNET.txt")


# 15 - Analise o arquivo "rede_INFNET_atualizado.txt" e identifique os 5 usuários que foram marcados como amigos pelo maior número de usuários cadastrados. Exiba o nome desses usuários e a quantidade de amigos que cada um possui.

contador_amigos = Counter()

with open(r"C:\python-infnet\python-dados-4t24\repositorio-python-para-dados-4t24-prof-dacio-souza-fabiolmorais\rede_INFNET_atualizado.txt", "r", encoding="utf-8") as rede_INFNET_autalizado:
  for linha in rede_INFNET_autalizado:
    if "Amigos:" in linha:
      amigos = linha.strip().split("Amigos: ")[1]
      if amigos != "Nenhum":
        lista_amigos = amigos.split(", ")
        contador_amigos.update(lista_amigos)

usuarios_popular = contador_amigos.most_common(5)

for nome, quantidade in usuarios_popular:
  print(f"{nome}: {quantidade} amigos")


# 16 - Explique com suas palavras a importância de utilizar o recurso ‘with’ ao lidar com arquivos em Python.

# Pelo o que entendi do with, ele fica responsável por abrir e fechar o arquivo, sendo assim, evitamos de fechar os arquivos toda hora que queremos fazer uma leitura ou escrita.