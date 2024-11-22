import pandas as pd
import csv
import json
import datetime as dt
import random
from IPython.display import display

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
  """Função criada para resover a questão 8 do enunciado: Criando Informações.
  Essa função não recebe nada como parâmetro e retorno df_atualizado

  Crio duas variaveis, uma para receber a função organizando_a_bagunça e outra para fazer o calculo do ano_nascimento
  No final adiciono a informação ano_nascimento na nova coluna e exporto um csv para verificar se deu certo.
  """
  df_atualizado = organizando_a_bagunca()

  ano_nascimento = dt.datetime.now().year - df_atualizado["Idade"]

  df_atualizado["ano_nascimento"] = ano_nascimento

  df_atualizado.to_csv("novos_usuarios.csv")

  return df_atualizado

def completando_os_dados():
  """Função criada para resover a questão 9 do enunciado: Completando os Dados.
  Essa função não recebe nada como parâmetro e retorno o df_atualizado

  Crio uma função para retornar um id aleatorio
  Depois utilizo uma função lambda para adicionar tanto o id, como o sobrenome não informado aos campos que tiverem valores ausentes
  Decidi incluir o id para todos os usuários tenham um identificador único, usei o mesmo criterio dos Id já existente
  E decidi incluir o sobrenome simplesmente pq não tinha outro campo como Id que fizesse tanto sentido adicionar a informação, pois os outros campos são informações pessoais, por isso a string "Não Informado"
  No final exporto um csv para verificar se deu certo e retorno o novo dataframe = df.
  """
  def gerar_id():
    """ função para retornar um id aleatorio

    Returns:
        string: uma string aleatoria
    """
    return "".join(random.choices("0123456789abcdefghijklmnopqrstuvxyz", k=8))

  df_atualizado = criando_informacoes()

  df_atualizado["Id"] = df_atualizado["Id"].apply(lambda x: gerar_id() if pd.isna(x) else x)
  df_atualizado["Sobrenome"] = df_atualizado["Sobrenome"].apply(lambda x: "Não Informado" if pd.isna(x) else x)

  df_atualizado.to_csv("novos_usuarios.csv")

  return df_atualizado

def guardando_as_informacoes():
  """Função criada para resover a questão 10 do enunciado: Guardando as Informações.
  Essa função não recebe nada como parâmetro e retorna nada

  Basicamente pego o dataframe mais atualizado e exporto o json conforme o enunciado pede.
  """

  df_atualizado = completando_os_dados()

  df_atualizado.to_json('fabio_morais_DR4_TP2/INFwebNet_Data.json', orient='records', indent=4, force_ascii=False)

def selecionando_grupos():
  """Função criada para resover a questão 11 do enunciado: Selecionando Grupos.
  Essa função não recebe nada como parâmetro e retorna nada

  Primeiramente acesso o json criado anteriormente para atualizar os dados para que fiquem na mesma estrutura, por exemplo: Pernambuco para PE.
  Depois faço o que o enunciado pede, primeiro crio uma função para tratar a string e deixa-la da forma que quero usando o split e replace, depois percorro o df["Estado"] para criar os arquivos de acordo com o filtro
  """

  with open("fabio_morais_DR4_TP2/INFwebNet_Data.json", "r", encoding="utf-8") as infwebnet_data:
    dados = json.load(infwebnet_data)

  for dado in dados:
    dado["Localização"] = dado["Localização"].replace("Pernambuco", "PE")

  with open("fabio_morais_DR4_TP2/INFwebNet_Data.json", "w", encoding="utf-8") as infwebnet_data_atualizado:
    json.dump(dados, infwebnet_data_atualizado, indent=4, ensure_ascii=False)

  df = pd.read_json("fabio_morais_DR4_TP2/INFwebNet_Data.json")

  def sigla_estado(localizacao):
    """função para tratar o df e deixar a string do jeito que quero

    Args:
        localizacao (df): o df contendo os dados

    Returns:
        string: uma string com o estado
    """
    estado = localizacao.split(", ")
    estado = estado[-1].replace(")", "").replace("'", "")
    return estado

  df["Estado"] = df["Localização"].apply(sigla_estado)

  for estado in df["Estado"].unique():
    df_estado = df[df["Estado"] == estado]

    nome_grupo = f"fabio_morais_DR4_TP2/grupo_{estado}.csv"
    df_estado.to_csv(nome_grupo, index=False, encoding="utf-8")

def agrupando_infnetianos():
  """Função criada para resover a questão 12 do enunciado: Agrupando INFNETianos.
  Essa função não recebe nada como parâmetro e retorna nada

  Primeiro leio o arquivo json, depois crio a função solicitada no enunciado.
  """
  df = pd.read_json("fabio_morais_DR4_TP2/INFwebNet_Data.json")

  def filtrar_por_ano(df, primeiro_ano, segundo_ano):
    """Função criada para filtrar os usuarios de acordo com os anos informados

    Args:
        df (dataframe): o df que tem os dados do usuario
        primeiro_ano (int): o ano inicial do filtro
        segundo_ano (int): o ano final do filtro
    Returns:
        dataframe: um novo df com os usuarios filtrados
    """
    df_filtrado = df[(df['ano_nascimento'] >= primeiro_ano) & (df['ano_nascimento'] <= segundo_ano)]
    
    display(df_filtrado)
    
    return df_filtrado
  
  filtrar_por_ano(df, 1996, 1999)

def selecionando_infnetianos():
  """Função criada para resover a questão 13 do enunciado: Selecionando INFNETiano.
  Essa função não recebe nada como parâmetro e retorna nada

  Primeiro leio o arquivo json, depois crio a função solicitada no enunciado.
  """
  df = pd.read_json("fabio_morais_DR4_TP2/INFwebNet_Data.json")

  def buscar_usuario(df, nome):
    """Busca um usuario pelo o nome e exibe-o, permitindo o usuario selecionar o INFNETiano.

    Args:
        df (dataframe): o dataframe com os dados dos usuarios
        nome (string): o nome do usuario
    """
    filtra_usuario_por_nome = df[df['Nome'].str.contains(nome, case=False, na=False)]

    if filtra_usuario_por_nome.empty:
      print("Nenhum usuario encontrado!")
      return
    
    if len(filtra_usuario_por_nome) > 1:
      print("Usuarios encontrados:")
      for index, (_, usuario) in enumerate(filtra_usuario_por_nome.iterrows(), start=1):
          print(f"{index}. {usuario['Nome']} - {usuario['Id']}")
      
      escolha = int(input(f"Escolha o número do usuário (1-{len(filtra_usuario_por_nome)}): ")) - 1
      
      if 0 <= escolha < len(filtra_usuario_por_nome):
          print("\nUsuario selecionado:")
          print(filtra_usuario_por_nome.iloc[escolha])
      else:
          print("Escolha inválida.")
    
    else:
      print("\nUsuario encontrado:")
      print(filtra_usuario_por_nome.iloc[0])
  
  nome = input("Digite o nome que queira buscar: ")
  buscar_usuario(df, nome)

def atualizando_dados():
  """Função criada para resover a questão 14 do enunciado: Atualizando Dados.
  Essa função não recebe nada como parâmetro e retorna nada

  Decidi criar outra função para fazer tudo do inicio e separar os enunciados, um para filtrar e outro para editar.
  """
  
  df = pd.read_json("fabio_morais_DR4_TP2/INFwebNet_Data.json")

  def editar_dados(usuario_selecionado, indice_usuario):
    """Função criada para editar os dados do usuario selecionado, como decidi refazer o código da função anterior, então eu tenho 2 formas pra editar os dados do usuário, a primeira é quando o nome filtrado só tem 1 e a segunda é que se tiver mais de um nome do filtrado, então o usuario tem que escolher qual quer editar. Pra não repetir o mesmo código, criei essa função

    Args:
        usuario_selecionado (dict): Dicionario contendo o usuário selecionado
        indice_usuario (int): Corresponde ao indice da linha no dataframe
    """
    print("\nDados disponíveis para atualização: ")
    dados = list(usuario_selecionado.keys())
    for index, dado in enumerate(dados, start=1):
      print(f"{index} - {dado}")

    dado_escolhido = int(input("\nDigite o número do dado que deseja atualizar: ")) - 1
    if 0 <= dado_escolhido < len(dados):
        dado = dados[dado_escolhido]
        if dado in ["Hobbies", "Jogos Favoritos"]:
          print(f"\nAtualizando {dado} **lembre-se, o máximo são 5**.")
          novos_dados = []
          for i in range(5):
            valor = input(f"Digite o {i+1}º {dado} ou pressione Enter para finalizar: ")
            if not valor:
              break
            novos_dados.append(valor)
          usuario_selecionado[dado] = novos_dados
        else:
          novo_valor = input(f"Digite o novo valor para {dado}: ")
          usuario_selecionado[dado] = novo_valor

        df.iloc[indice_usuario] = usuario_selecionado
        df.to_json("fabio_morais_DR4_TP2/INFwebNet_Data.json", orient='records', indent=4, force_ascii=False)
    
    else:
      print("Escolha inválida.")

  def atualizar_dados_usuario(df, nome):
    """Busca um usuario pelo o nome e exibe-o, permitindo o usuario atualizar os dados do INFNETiano.

    Args:
        df (dataframe): o dataframe com os dados dos usuarios
        nome (string): o nome do usuario
    """
    filtra_usuario_por_nome = df[df['Nome'].str.contains(nome, case=False, na=False)]

    if filtra_usuario_por_nome.empty:
      print("Nenhum usuario encontrado!")
      return
    
    if len(filtra_usuario_por_nome) > 1:
      print("Usuarios encontrados:")
      for index, (_, usuario) in enumerate(filtra_usuario_por_nome.iterrows(), start=1):
          print(f"{index}. {usuario['Nome']} - {usuario['Id']}")
      
      escolha = int(input(f"Escolha o número do usuário (1-{len(filtra_usuario_por_nome)}) que deseja atualizar: ")) - 1
      
      if 0 <= escolha < len(filtra_usuario_por_nome):
          usuario_selecionado = filtra_usuario_por_nome.iloc[escolha].to_dict()
          editar_dados(usuario_selecionado, filtra_usuario_por_nome.index[escolha])
      else:
          print("Escolha inválida.")
    
    else:
      print("\nUsuario encontrado:")
      usuario_selecionado = filtra_usuario_por_nome.iloc[0].to_dict()
      editar_dados(filtra_usuario_por_nome, filtra_usuario_por_nome.index[0])
  
  nome = input("Digite o nome que queira buscar: ")
  atualizar_dados_usuario(df, nome)

def trending():
  """Função criada para resover a questão 15 do enunciado: Trending.
  Essa função não recebe nada como parâmetro e retorna nada

  Primeiro leio o json.
  Depois uso o fillna para remover as lingugens de programação que não tem nada, ou seja, são Null, NaN, etc.
  Depois crio uma lista de linguagens vazia.
  Depois percorro o df e trato os dados para incluir na lista criada anteriormente.
  Depois crio uma variavel para contar a quantidade de vezes que uma linguagem se repete, utilizo o values_count para isso.
  No fim, percorro a lista para imprimir as 5 mais citadas, conforme pede o enunciado.
  """
  df = pd.read_json("fabio_morais_DR4_TP2/INFwebNet_Data.json")

  df['Linguagem de Programação'] = df['Linguagem de Programação'].fillna('')

  linguagens = []

  for index, linha in df.iterrows():
    lista_linguagens = linha["Linguagem de Programação"]

    if lista_linguagens:
      linguagens += [linguagem.strip() for linguagem in lista_linguagens.split(",") if linguagem != "[]"]

  contagem_linguagens = pd.Series(linguagens).value_counts()

  print("\nAs 5 linguagens mais citadas:")
  for i, (linguagem, contagem) in enumerate(contagem_linguagens.head(5).items(), start=1):
    print(f"{i} - {linguagem}: {contagem}")

abrindo_as_portas()
estruturando_os_dados()
cadastro_simplificado()
analise_com_pandas()
ampliando_as_informacoes()
dados_delimitados()
organizando_a_bagunca()
criando_informacoes()
completando_os_dados()
guardando_as_informacoes()
selecionando_grupos()
agrupando_infnetianos()
selecionando_infnetianos()
atualizando_dados()
trending()