import pandas as pd
import csv
import json
import datetime as dt

def abrindo_as_portas():
  """Função criada para resover a questão 1 do enunciado: Abrindo as Portas.
  Essa função não recebe nada como parâmetro e nem retorna nada

  Criei uma lista usuarios para adicionar todos os usuarios do arquivo txt lido
  Fiz a leitura e para cada linha tratei os dados individualmente para que o csv fique com os dados corretos
  Após isso, criei um dataframe com o pandas para facilitar a criação do arquivo csv, conforme pede a questão
  No final imprime a mensagem de que o arquivo foi exportado com sucesso.
  """

  usuarios = []

  with open(r"C:\python-infnet\python-dados-4t24\repositorio-python-para-dados-4t24-prof-dacio-souza-fabiolmorais\rede_INFNET_atualizado.txt", "r", encoding="utf-8") as arquivo_txt:
    leitor = arquivo_txt.readlines()

    for linha in leitor:
      dados = linha.strip().split(', ')

      nome = dados[0].split(": ")
      nome_tratado = nome[1] if nome[1] else None

      idade = dados[1].split(": ")
      idade_tratada = int(idade[1]) if idade[1].isdigit() else None

      cidade = dados[2].replace("Localização: ", "") if dados[2] else None

      estado = dados[3] if dados[3] else None

      amigos = dados[4:]
      amigos_tratado = amigos[1:]

      if len(amigos) == 1:
        amigos_tratado = amigos[0].replace("Amigos: ", "")
      else:
        amigos_tratado.insert(0, amigos[0].replace("Amigos: ", ""))

      usuario = {
        "Nome": nome_tratado,
        "Idade": idade_tratada,
        "Localização": (cidade, estado),
        "Amigos": amigos_tratado
      }

      usuarios.append(usuario)


  df_txt = pd.DataFrame(usuarios)

  arquivo_csv = "./fabio_morais_DR4_TP2/INFwebNet.csv"

  with open(arquivo_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(df_txt.columns)
    for _, row in df_txt.iterrows():
      writer.writerow(row)

  print("CSV exportado com sucesso!!")

def estruturando_os_dados():
  """Função criada para resover a questão 2 do enunciado: Estruturando os Dados.
  Essa função não recebe nada como parâmetro e nem retorna nada

  Criei uma lista usuarios para adicionar todos os usuarios do arquivo csv lido
  Após isso, parseiei (sei nem se essa palavra existe) as informações para estrutura json e exportei devidamente estruturado
  No final imprime a mensagem de que o arquivo foi exportado com sucesso.
  """
  usuarios = []

  arquivo_json = "./fabio_morais_DR4_TP2/INFwebNet.json"

  with open("./fabio_morais_DR4_TP2/INFwebNet.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
      usuarios.append(linha)

  with open(arquivo_json, "w", encoding="utf-8") as jsonfile:
    json.dump(usuarios, jsonfile, indent=4, ensure_ascii=False)

  print("JSON exportado com sucesso!!")

def cadastro_simplificado():
  """Função criada para resover a questão 3 do enunciado: Cadastro Simplificado.
  Essa função não recebe nada como parâmetro e nem retorna nada

  Primeiro carrego o arquivo json
  Depois eu começo a coletar os dados com suas validações
  Nome não pode ser uma entrada vazia nem dado os espaços (Ex:     ) e se o usuário adicionar espaços em branco no inicio e no fim são removidos, por isso o metodo strip
  Idade não pode ser texto, numero negativo e nem numero float
  Cidade e estado é a mesma coisa do nome
  No final crio outro arquivo json com os novos dados e imprimo a mensagem de que o usuário foi adicionado com sucesso.
  """
  with open('./fabio_morais_DR4_TP2/INFwebNet.json', 'r', encoding='utf-8') as arquivo_json:
    usuarios = json.load(arquivo_json)

  while True:
    nome = input("Digite o nome do INFNETiano: ").strip()
    if nome:
      break
    print("Entrada inválida. O nome não pode ser vazio")

  while True:
    try:
      idade = int(input("Digite a idade do INFNETiano: "))
      if idade > 0:
        break
      else:
        print("Entrada inválida. A idade deve ser maior que zero.")
    except ValueError:
      print("Entrada inválida. Insira um número inteiro.")

  while True:
    cidade = input("Digite a cidade do INFNETiano: ").strip()
    if cidade:
      break
    print("Entrada inválida. A cidade não pode ser vazia.")
  
  while True:
    estado = input("Digite o estado do INFNETiano: ").strip()
    if estado:
      break
    print("Entrada inválida. O estado não pode ser vazio.")

  novo_usuario = {
    "Nome": nome,
    "Idade": idade,
    "Localização": f"('{cidade}', '{estado}')",
    "Amigos": []
  }

  usuarios.append(novo_usuario)

  with open("./fabio_morais_DR4_TP2/INFwebNet.json", "w", encoding="utf-8") as jsonfile:
    json.dump(usuarios, jsonfile, indent=4, ensure_ascii=False)

  print("Usuário adicionado com sucesso!")

def analise_com_pandas():
  """Função criada para resover a questão 4 do enunciado: Análise com Pandas.
  Essa função não recebe nada como parâmetro e nem retorna nada

  Primeiro leio o arquivo json e adiciono os dados na variavel df
  Calculo a media com o metodo mean, segue referencia: https://www.geeksforgeeks.org/python-pandas-dataframe-mean/
  No final imprimo a mensagem com a media das idades.
  """
  df = pd.read_json("./fabio_morais_DR4_TP2/INFwebNet.json")
  media_idade = df["Idade"].mean()
  print(f"A média das idades é: {media_idade:.2f}")
  
def ampliando_as_informacoes():
  """Função criada para resover a questão 5 do enunciado: Ampliando as Informações.
  Essa função não recebe nada como parâmetro e nem retorna nada

  Primeiro carrego o arquivo json
  Depois solicito os dados ao usuário com suas validações
  Depois gero um novo arquivo json com os novos dados
  No final imprimo a mensagem de usuário adicionado.
  """

  with open('./fabio_morais_DR4_TP2/INFwebNet.json', 'r', encoding='utf-8') as arquivo_json:
    usuarios = json.load(arquivo_json)

  while True:
    nome = input("Digite o nome do INFNETiano: ").strip()
    if nome:
      break
    print("Entrada inválida. O nome não pode ser vazio")

  while True:
    try:
      idade = int(input("Digite a idade do INFNETiano: "))
      if idade > 0:
        break
      else:
        print("Entrada inválida. A idade deve ser maior que zero.")
    except ValueError:
      print("Entrada inválida. Insira um número inteiro.")

  while True:
    cidade = input("Digite a cidade do INFNETiano: ").strip()
    if cidade:
      break
    print("Entrada inválida. A cidade não pode ser vazia.")
  
  while True:
    estado = input("Digite o estado do INFNETiano: ").strip()
    if estado:
      break
    print("Entrada inválida. O estado não pode ser vazio.")

  while True:
    hobbies = []
    try:
      escolha = int(input("Quer adicionar algum hobby? Se sim, digite 1, se não digite 2: "))
      while escolha == 1:
        hobbies.append(input("Digite um hobby por vez: ").strip())
        escolha = int(input("Quer adicionar outro hobby? Se sim, digite 1, se não digite 2: "))
        if escolha == 2:
          break
        if escolha != 1 and escolha != 2:
          print("Entrada inválida. Digite apenas 1 ou 2.")
      if escolha == 2:
          break
      if escolha != 1 and escolha != 2:
          print("Entrada inválida. Digite apenas 1 ou 2.")

    except ValueError:
      print("Entrada inválida. Digite 1 se quiser adicionar hobby ou 2 se não quiser adicionar.")

  while True:
    coding = []
    try:
      escolha = int(input("Quer adicionar alguma linguagem de programação? Se sim, digite 1, se não digite 2: "))
      while escolha == 1:
        coding.append(input("Digite uma linguagem por vez: ").strip())
        escolha = int(input("Quer adicionar outra linguagem? Se sim, digite 1, se não digite 2: "))
        if escolha == 2:
          break
        if escolha != 1 and escolha != 2:
          print("Entrada inválida. Digite apenas 1 ou 2.")
      if escolha == 2:
          break
      if escolha != 1 and escolha != 2:
          print("Entrada inválida. Digite apenas 1 ou 2.")

    except ValueError:
      print("Entrada inválida. Digite 1 se quiser adicionar uma linguagem ou 2 se não quiser adicionar.")


  while True:
    jogos = {}
    try:
      escolha = int(input("Quer adicionar algum jogo? Se sim, digite 1, se não digite 2: "))
      while escolha == 1:
        nome_jogo_favorito = input("Digite o nome do jogo favorito: ").strip()
        plataforma = input("Digite o nome da plataforma que você jogou esse jogo: ").strip()
        jogos.update({nome_jogo_favorito: plataforma})
        escolha = int(input("Quer adicionar outro jogo? Se sim, digite 1, se não digite 2: "))
        if escolha == 2:
          break
        if escolha != 1 and escolha != 2:
          print("Entrada inválida. Digite apenas 1 ou 2.")
      if escolha == 2:
          break
      if escolha != 1 and escolha != 2:
          print("Entrada inválida. Digite apenas 1 ou 2.")

    except ValueError:
      print("Entrada inválida. Digite 1 se quiser adicionar uma linguagem ou 2 se não quiser adicionar.")
    
  novo_usuario = {
    "Nome": nome,
    "Idade": idade,
    "Localização": f"('{cidade}', '{estado}')",
    "Amigos": [],
    "Hobbies": hobbies,
    "Linguagem de Programação": coding,
    "Jogos Favoritos": jogos
  }

  usuarios.append(novo_usuario)

  with open("./fabio_morais_DR4_TP2/INFwebNet.json", "w", encoding="utf-8") as jsonfile:
    json.dump(usuarios, jsonfile, indent=4, ensure_ascii=False)

  print("Usuário adicionado com sucesso!")

def dados_delimitados():
  """Função criada para resover a questão 6 do enunciado: Dados Delimitados.
  Essa função não recebe nada como parâmetro e retorna a lista de novos usuarios

  Crio uma variavel novos_usuarios para adicionar os usuarios lido do arquivo para testar se foi lido de forma correta
  Depois leio o arquivo dados_usuarios_novos.txt com o modulo csv
  Adiciono o usuario a lista novos_usuarios
  No final imprimo a lista de novos_usuarios para validar.
  """
  novos_usuarios = []

  with open("../repositorio-python-para-dados-4t24-prof-dacio-souza-fabiolmorais/dados_usuarios_novos.txt", "r", encoding="utf-8") as arquivo_txt:
    leitor = csv.reader(arquivo_txt, delimiter=";")
    cabecalho = next(leitor)
    for linha in leitor:
      
      id = linha[0] if linha[0] else None
      nome = linha[1] if linha[1] else None
      sobrenome = linha[2] if linha[2] else None
      email = linha[3] if linha[3] else None
      idade_float = float(linha[4]) if linha[4] != "" else None
      idade = int(idade_float) if idade_float != None else None
      data_nascimento = linha[5] if linha[5] else None
      cidade = linha[6] if linha[6] else None
      estado = linha[7] if linha[7] else None
      hobbies = linha[8] if len(linha[8]) > 0 else []
      linguagem_programacao = linha[9] if len(linha[9]) > 0 else []
      jogos = linha[10] if len(linha[10]) > 0 else {}

      usuario = {
        "Id": id,
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Email": email,
        "Idade": idade,
        "Data de Nascimento": data_nascimento,
        "Localização": f"('{cidade}', '{estado}')",
        "Hobbies": hobbies,
        "Linguagem de Programação": linguagem_programacao,
        "Jogos Favoritos": jogos
      }

      novos_usuarios.append(usuario)

  return novos_usuarios

def organizando_a_bagunca():
  """Função criada para resover a questão 7 do enunciado: Organizando a Bagunça.
  Essa função não recebe nada como parâmetro e retorna o dataframe com todas as informações reunidas

  Crio duas variaveis, uma para ler o arquivo json com o pandas e outra para criar um dataframe baseado na leitura da questão 6
  Depois junto os dois dataframes com o metodo concat
  No final imprimo o dataframe criado.
  """
  df_json = pd.read_json("./fabio_morais_DR4_TP2/INFwebNet.json")
  df_novos_usuarios = pd.DataFrame(dados_delimitados())

  df_atualizado = pd.concat([df_json,df_novos_usuarios], ignore_index=True)
  return df_atualizado

def criando_informacoes():
  df_atualizado = organizando_a_bagunca()

  ano_nascimento = dt.datetime.now().year - df_atualizado["Idade"]

  df_atualizado["ano_nascimento"] = ano_nascimento

  print(df_atualizado)


abrindo_as_portas()
estruturando_os_dados()
#cadastro_simplificado()
#analise_com_pandas()
#ampliando_as_informacoes()
dados_delimitados()
organizando_a_bagunca()
criando_informacoes()