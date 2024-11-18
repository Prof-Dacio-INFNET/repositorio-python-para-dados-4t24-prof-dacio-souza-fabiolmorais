import pandas as pd
import csv

df_txt = pd.read_csv("../rede_INFNET_atualizado.txt", sep="/t")

print(df_txt)

arquivo_csv = "INFwebNet.csv"

with open(arquivo_csv, "w", newline="", encoding="latin1") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(df_txt.columns)
  for _, row in df_txt.iterrows():
    writer.writerow(row)

print("CSV exportado com sucesso!!")


