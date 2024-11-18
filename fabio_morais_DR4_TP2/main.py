import pandas as pd
import csv
import json

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
        "nome": nome_tratado,
        "idade": idade_tratada,
        "localização": (cidade, estado),
        "amigos": amigos_tratado
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
  usuarios = []

  with open("INFwebNet.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
      usuarios.append(linha)

estruturando_os_dados()
abrindo_as_portas()