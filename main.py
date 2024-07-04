import requests, csv
import pandas as pd
import os



url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-2019%27&@dataFinalCotacao=%2712-31-2025%27&$top=9000&$format=text/csv&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao'
api_banco = pd.read_csv(url)
print(api_banco)

caminho = "DataLake\Bronze"

caminho_destino = os.path.join(caminho, "Dados.csv")

if not os.path.exists(caminho):
    os.makedirs(caminho)
api_banco['cotacaoCompra'] = api_banco['cotacaoCompra'].str.replace(',', '.').astype(float)
api_banco['cotacaoVenda'] = api_banco['cotacaoVenda'].str.replace(',', '.').astype(float)
api_banco['dataHoraCotacao'] = pd.to_datetime(api_banco['dataHoraCotacao'])

api_banco.to_csv(caminho_destino, index=False)