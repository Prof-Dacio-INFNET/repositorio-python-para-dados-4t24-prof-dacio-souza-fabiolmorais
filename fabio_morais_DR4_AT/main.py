import pandas as pd
import urllib.request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import os
import re
import json
from typing import List, Dict
from sqlalchemy import create_engine
import sqlite3


def carregar_dados():
  """Carrega dados do arquivo INFwebNet_Data.json conforme solicitado no enunciado.

  Raises:
      FileNotFoundError: Gera esse erro se o arquivo não for encontrado
      ValueError: Gera esse erro se o arquivo não tiver as colunas esperadas
      ValueError: _description_

  Returns:
      DataFrame: df contendo os dados do arquivo
  """

  arquivo = "fabio_morais_DR4_TP2/INFwebNet_Data.json"

  try:
    with open(arquivo, 'r', encoding='utf-8') as file:
      df = pd.read_json(file)
  except FileNotFoundError:
    raise FileNotFoundError("Arquivo não foi encontrado")
  except ValueError as e:
    raise ValueError("Erro ao carregar o arquivo")
  
  colunas_esperadas = ["Nome", "Idade", "Localização", "Amigos", "Id", "Sobrenome", "Email", "Data de Nascimento", "Hobbies", "Linguagem de Programação", "Jogos Favoritos", "ano_nascimento"]
  for coluna in colunas_esperadas:
    if coluna not in df.columns:
      raise ValueError(f"Coluna esperada {coluna} está ausente.")
  
  df = df.fillna("Não Informado")

  return df

def extrair_plataformas(df):
  """Extrai os nomes das plataformas de jogos, conforme enunciado pede.

  Args:
      df (pd.DataFrame): DataFrame retornado pela função carregar_dados.

  Returns:
      set: Conjunto com os nomes das plataformas
  """

  plataformas = set()
  if "Jogos Favoritos" in df.columns:
    for item in df["Jogos Favoritos"]:
      try:
        jogos = eval(item)
        if isinstance(jogos, list):
          plataformas.update([jogo[1] for jogo in jogos if len(jogo) == 2])
      except (ValueError, SyntaxError):
        pass

  with open("plataformas.txt", "w", encoding="utf-8") as arquivo:
    for plataforma in sorted(plataformas):
      arquivo.write(f"{plataforma}\n")

  return plataformas

def carregar_plataformas():
  """Tenta carregar o arquivo plataformas.txt e retorna uma lista com os nomes das plataformas, conforme pede o enunciado.

  Returns:
      list: Lista com os nomes das plataformas.
  """

  while True:
    try:
      with open("plataformas.txt", "r", encoding="utf-8") as arquivo:
        plataformas = [linha.strip() for linha in arquivo.readlines()]
      return plataformas
    except FileNotFoundError:
      print("Arquivo não foi encontrado.")
      novo_caminho = input("Digite o caminho correto do arquivo ou digite 'sair' para encerrar o programa:")
      if novo_caminho.lower() == 'sair':
        print("Encerrando o programa...")
        break
      else:
        try:
          with open("plataformas.txt", "r", encoding="utf-8") as arquivo:
            plataformas = [linha.strip() for linha in arquivo.readlines()]
          return plataformas
        except FileNotFoundError:
          print("Arquivo não foi encontrado.")


# função baixar paginas com o erro

# def baixar_paginas_wikipedia(plataformas):
#   """Faz o download das páginas da wikipédia de cada plataforma e salva em arquivos HTML, conforme pede o enunciado.

#   Args:
#       plataformas (list): Lista de nomes das plataformadas retornadas pela a função carregar_plataformas.

#   Returns:
#       list: Lista com os caminhos dos arquivos gerados.
#   """


#   caminhos = []

#   for plataforma in plataformas:
#     nome_formatado = plataforma.replace(" ", "_")
#     url = f"https://pt.wikipedia.org/wiki/Lista_de_jogos_para_{nome_formatado}"
#     print(url)

#     caminho_arquivo = f"plataforma_{nome_formatado}.html"

#     try:
#       with urllib.request.urlopen(url) as resposta:
#         conteudo = resposta.read()

#       with open(caminho_arquivo, "wb") as arquivo:
#         arquivo.write(conteudo)

#       caminhos.append(caminho_arquivo)
#     except Exception as e:
#       print(f"ERROR: Na tentativa de baixar ou salvar a página {plataforma} gerou o erro: {e}")

#   return caminhos

# 5 questão
def baixar_paginas_wikipedia(plataformas):
  """Faz o download das páginas da wikipédia de cada plataforma e salva em arquivos HTML, conforme pede o enunciado.

  Args:
      plataformas (list): Lista de nomes das plataformadas retornadas pela a função carregar_plataformas.

   Returns:
      list: Lista com os caminhos dos arquivos gerados.
  """

  caminhos = []

  with open("erros_download.txt", "w", encoding="utf-8") as erros:
    for plataforma in plataformas:
      nome_formatado = plataforma.replace(" ", "_")
      url = f"https://pt.wikipedia.org/wiki/Lista_de_jogos_para_{nome_formatado}"

      caminho_arquivo = f"plataforma_{nome_formatado}.html"

      try:
        with urllib.request.urlopen(url) as resposta:
          conteudo = resposta.read()

        with open(caminho_arquivo, "wb") as arquivo:
          arquivo.write(conteudo)

        caminhos.append(caminho_arquivo)

      except HTTPError as e:
        erros.write(f"Plataforma: {plataforma} - HTTPError: {e.code} - {e.reason}\n")

      except URLError as e:
        erros.write(f"Plataforma: {plataforma} - URLError: {e.reason}\n")

      except Exception as e:
        erros.write(f"Plataforma: {plataforma} - Erro inesperado: {e}\n")

  return caminhos

def parsear_paginas(caminho_arquivo):
  """Parseia o conteúdo HTML de um arquivo, valida o título da página e extrai tabelas de jogos, conforme pede o enunciado.

  Args:
      caminho_arquivo (str): Caminho para o arquivo HTML

  Raises:
      ValueError: Se o título da página estiver errado

  Returns:
      dict: Dados extraídos.
  """

  try:
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
      conteudo = arquivo.read()

    soup = BeautifulSoup(conteudo, "html.parser")
    titulo = soup.title.string.strip()

    plataforma_nome = caminho_arquivo.split("_")[1].replace(".html", "").replace("_", " ")
    if plataforma_nome.lower() not in titulo.lower():
      with open("erros_parse.txt", "a", encoding="utf-8") as erros:
        erros.write(f"O título '{titulo}' não corresponde a plataforma '{plataforma_nome}' no arquivo {caminho_arquivo}")
      raise ValueError(f"Título '{titulo}' não corresponde a plataforma '{plataforma_nome}'")

    # Enunciado 7
    tabelas = soup.find_all("table", class_="wikitable")
    dados_extraidos = []

    for tabela in tabelas:
      headers = [th.get_text(strip=True) for th in tabela.find_all("th")]
      linhas = tabela.find_all("tr")[1:]

      for linha in linhas:
        colunas = linha.find_all("td")
        if colunas:
          dados = {headers[i]: colunas[i].get_text(strip=True) for i in range(len(colunas)) if i < len(headers)}
          dados_extraidos.append(dados)

      return {
        "titulo": titulo,
        "dados": dados_extraidos
      }
    
  except Exception as e:
    with open("erros_parse.txt", "a", encoding="utf-8") as erros:
      erros.write(f"Erro ao parsear o arquivo {caminho_arquivo} - {e}\n")
    raise

def extrair_urls_emails():
  """Busca no diretorio arquivos que começam com plataforma e termina com html, extrai as urls e e-mails e salva no arquivo json conexoes_plataformas.json
  """

  dados_conexoes = {"urls": set(), "e-mails": set()}

  # regex_email = r"^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$"
  # regex_url = r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[.\!\/\\w]*))?)"

  #https://regexr.com/39nr7
  #https://regexr.com/3e48o

  # quando fiz a função com os regex passados no enunciado não achou nenhum, busquei por regex na internet e achei os 2 links acima, mesmo assim o regex do email não encontrou nada e o da url está errado.

  regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
  regex_url = r"https?://(?:www\.)?[a-zA-Z0-9./?=&_%+-]+"


  for caminho in [arquivo for arquivo in os.listdir() if arquivo.startswith("plataforma_") and arquivo.endswith(".html")]:
    try:
      with open(caminho, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        soup = BeautifulSoup(conteudo, "html.parser")

        for link in soup.find_all("a", href=True):
          match = re.match(regex_url, link["href"])
          if match:
            dados_conexoes["urls"].add(match.group(0))

        for texto in soup.find_all(string=True):
          match_email = re.search(regex_email, texto)
          if match_email:
            dados_conexoes["e-mails"].add(match_email.group())

    except Exception as e:
      with open("erros_extracao.txt", "a", encoding="utf-8") as erros:
        erros.write(f"Erro no arquivo '{caminho}' - {e}")
    
  dados_conexoes["urls"] = list(dados_conexoes["urls"])
  dados_conexoes["e-mails"] = list(dados_conexoes["e-mails"])

  with open("conexoes_plataformas.json", "w", encoding="utf-8") as json_file:
    json.dump(dados_conexoes, json_file, ensure_ascii=False, indent=4)


def exportar_dados_jogos(dados_jogos):
  """Exporta os dados dos jogos para o arquivo JSON conforme pede o enunciado

  Args:
      dados_jogos (List[Dict]): Lista contendo os dados dos jogos
  """

  dados_formatados = []

  for categoria in dados_jogos:
    plataforma = categoria.get("titulo", "Plataforma_Desconhecida")
    jogos_da_plataforma = categoria.get("dados", [])

    jogos_formatados = []
    for jogo in jogos_da_plataforma:
      nome_jogo = jogo.get("Título", "Jogo_Desconhecido")
      dados_jogo = {chave: valor for chave, valor in jogo.items() if chave != "Título"}

      jogos_formatados.append({
        "nome_jogo": nome_jogo,
        "dados_jogo": dados_jogo
      })

    dados_formatados.append({
      "plataforma": plataforma,
      "jogos": jogos_formatados
    })

  try:
    with open("dados_jogos_plataformas.json", mode="w", encoding="utf-8") as jsonfile:
      json.dump(dados_formatados, jsonfile, indent=4, ensure_ascii=False)
  except Exception as e:
    print(f"Erro ao exportar o arquivo JSON: {e}")

def associar_jogos_usuarios(df_usuarios: pd.DataFrame, dados_jogos: List[Dict]) -> pd.DataFrame:
  """Associa os jogos aos usuários

  Args:
      df_usuarios (pd.DataFrame): DataFrame com os dados dos usuários
      dados_jogos (List[Dict]): Lista de dicionários com jogos extraidos

  Returns:
      pd.DataFrame: DataFrame atualizado com as associações
  """

  associacoes = []

  jogos_por_plataforma = {}
  for plataforma in dados_jogos:
    for jogo in plataforma["dados"]:
      nome_jogo = jogo.get("Título", "").strip().lower()

  for _, usuario in df_usuarios.iterrows():
    jogos_usuario = usuario.get("Jogos Favoritos", [])
    try:
      if isinstance(jogos_usuario, str):
        jogos_usuario = eval(jogos_usuario)
    except (ValueError, SyntaxError):
      jogos_usuario = []
      with open("erros_associacao.txt", "a", encoding="utf-8") as log_erros:
        log_erros.write(f"Dado inválido para o usuário {usuario['Nome']}: {jogos_usuario}\n")

    associacao_usuario = []
    for item in jogos_usuario:
      if isinstance(item, (tuple, list)) and len(item) == 2:
        jogo, plataforma = item
        nome_jogo_normalizado = jogo.strip().lower()
        plataforma_associada = jogos_por_plataforma.get(nome_jogo_normalizado, "Não Encontrado")
        associacao_usuario.append({"jogo": jogo, "plataforma": plataforma_associada})
      else:
        with open("erros_associacao.txt", "a", encoding="utf-8") as erros:
          erros.write(f"Item inválido para o usuário {usuario['Nome']}: {item}\n")

    associacoes.append(associacao_usuario)

  df_usuarios["Associações Jogos"] = associacoes

  return df_usuarios

def atualizar_banco_dados(df_usuarios_atualizados):
  """Atualzia o bd adicionando a tabela conforme pede o enunciado da questão

  Args:
      df_usuarios_atualizados (DataFrame): DataFrame que contém todos os dados dos usuarios atualizados.
  """

  df = pd.DataFrame(df_usuarios_atualizados)

  for coluna in ["Nome", "Idade", "Localização", "Amigos", "Id", "Sobrenome", "Email", "Data de Nascimento", "Hobbies", "Linguagem de Programação", "Jogos Favoritos", "ano_nascimento", "Associações Jogos"]:
    df[coluna] = df[coluna].apply(json.dumps)

  try:

    engine = create_engine('sqlite:///INFwebNET_DB.db')

    df.to_sql("Jogos_Plataformas", con=engine, if_exists="replace", index=False)

    print("Tabela criada com sucesso!")

  except Exception as e:
    print(f"ERROR: Erro ao tentar criar a tabela: {e}")

def consultar_usuarios_por_jogo():
  """Consulta os usuarios por jogo passado pelo o input

  Args:
      None.
  """

  nome_jogo = input("Digite o nome do jogo para realizar a busca: ").strip()

  try:
    conn = sqlite3.connect("INFwebNET_DB.db")
    cursor = conn.cursor()

    query = """
      SELECT nome, `Jogos Favoritos`
      FROM Jogos_Plataformas
    """
    cursor.execute(query)
    resultados = cursor.fetchall()

    usuarios_encontrados = []
    for nome, jogos_favoritos in resultados:
      jogos_favoritos = eval(jogos_favoritos)
      jogos_lista = []
      jogos_lista.append(jogos_favoritos)

      if any(nome_jogo.lower() in jogo.lower() for jogo in jogos_lista):
        usuarios_encontrados.append(nome)

    if usuarios_encontrados:
      print(f"Usuários que jogam {nome_jogo}:")
      for nome in usuarios_encontrados:
        print(f"- {nome}")

    else:
      print("Nenhum usuário encontrado.")

  except sqlite3.Error as e:
    print(f"Erro ao acessar o banco: {e}")

  finally:
    if conn:
      conn.close()

def plataforma_mais_popular():

  try:
    conn = sqlite3.connect("INFwebNET_DB.db")
    cursor = conn.cursor()

    query = """
      SELECT `Jogos Favoritos`
      FROM Jogos_Plataformas
    """
    cursor.execute(query)
    resultados = cursor.fetchall()

    contador_pc = 0
    contador_xbox_one = 0
    contador_playstation = 0
    contador_mobile = 0
    contador = {}

    for resultado in resultados:
      lista_resulado = list(resultado)

      for re in lista_resulado:
        if "PC" in re:
          contador_pc += 1

        if "Xbox One" in re:
          contador_xbox_one += 1

        if "PlayStation 4" in re:
          contador_playstation += 1

        if "Mobile" in re:
          contador_mobile += 1
        
    contador["PC"] = contador_pc    
    contador["Xbox One"] = contador_xbox_one    
    contador["PlayStation 4"] = contador_playstation    
    contador["Mobile"] = contador_mobile    

    plataforma_mais_popular = max(contador, key=contador.get)

    print(f'A plataforma mais popular é: {plataforma_mais_popular} com {contador[plataforma_mais_popular]} usuários.')

  
  except sqlite3.Error as e:
    print(f"Erro ao acessar o banco: {e}")

  finally:
    if conn:
      conn.close()

def salvar_dados_completos(df_usuarios_atualizados: pd.DataFrame):

  usuarios_completos = []

  for _, usuario in df_usuarios_atualizados.iterrows():
    usuario_dados = {
      "Nome": usuario.get("Nome", "Não Informado"),
      "Idade": usuario.get("Idade", "Não Informado"),
      "Localização": usuario.get("Localização", "Não Informado"),
      "Amigos": usuario.get("Amigos", "Não Informado"),
      "Id": usuario.get("Id", "Não Informado"),
      "Sobrenome": usuario.get("Sobrenome", "Não Informado"),
      "Email": usuario.get("Email", "Não Informado"),
      "Data de Nascimento": usuario.get("Data de Nascimento", "Não Informado"),
      "Hobbies": usuario.get("Hobbies", "Não Informado"),
      "Linguagem de Programação": usuario.get("Linguagem de Programação", "Não Informado"),
      "Jogos": usuario.get("Associações Jogos", [])
    }

    usuarios_completos.append(usuario_dados)

  with open("INFwebNET_Completo.json", "w", encoding="utf-8") as json_file:
    json.dump(usuarios_completos, json_file, ensure_ascii=False, indent=4)



if __name__ == "__main__":
  try:
    dados = carregar_dados()
    print("Dados carregados com sucesso!")

    extrair_plataformas(dados)
    print("Plataforma extraída com sucesso!")

    plataformas = carregar_plataformas()
    print("Plataforma carregada com sucesso!")

    caminho_arquivo = baixar_paginas_wikipedia(plataformas)
    print("Páginas baixadas com sucesso!")
    
    dados_jogos = []
    for caminho in caminho_arquivo:
      dados_jogos.append(parsear_paginas(caminho))
      print("Páginas parseada com sucesso!")

    extrair_urls_emails()
    print("URL's extraidas com sucesso!")

    dados_formatados = exportar_dados_jogos(dados_jogos)
    print("Dados exportados com sucesso!")

    df_usuarios_atualizados = associar_jogos_usuarios(dados, dados_jogos)
    print("Dados associados com sucesso!")

    atualizar_banco_dados(df_usuarios_atualizados)
    print("Dados associados com sucesso!")

    consultar_usuarios_por_jogo()
    print("Consulta realizada com sucesso!")

    plataforma_mais_popular()
    print("Consulta realizada com sucesso!")

    salvar_dados_completos(df_usuarios_atualizados)
    print("Dados salvos com sucesso!")

    

  except Exception as e:
    print(f"ERROR: {e}")