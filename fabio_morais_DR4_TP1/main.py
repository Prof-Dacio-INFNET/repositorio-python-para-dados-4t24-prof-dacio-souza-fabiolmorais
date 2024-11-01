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

print("=============== Perfis válidos após 4° questão =======================")
print(perfis_validos)

# 6 - Com os dados carregados no exercício anterior, adicione os usuários dos exercícios 1 e 2, definindo um padrão para lidar com os dados ausentes e salve estas informações em um arquivo "rede_INFNET.txt".

for perfil in perfis:
  perfil['amigos'] = []

print("")
print("=============== Perfis 6° questão =======================")
print(perfis)
print("")

perfis_validos.extend(perfis)

print("=============== Perfis válidos 6° questão =======================")
print(perfis_validos)

with open("rede_INFNET.txt", "w", encoding="UTF-8") as rede_INFNET:
  for perfil in perfis_validos:
    escritor = (
      f"Nome: {perfil['nome']}, "
      f"Idade: {perfil['idade']}, "
      f"Localização: {perfil['localização'][0]}, {perfil['localização'][1]}, "
      f"Amigos: {', '.join(perfil['amigos']) if perfil['amigos'] else 'Nenhum'}\n"
    )
    rede_INFNET.write(escritor)

print("Dados salvos com sucesso!!!")