import time
from loguru import logger
import yfinance as yf
import pandas as pd 


# Lista de commodities
commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata
logger.add("file_{time}.log")

def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    start_time = time.time()
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo  # Adiciona a coluna do símbolo
    logger.info(dados)
    logger.info("--- %s seconds ---" % (time.time() - start_time))
    return dados

def buscar_todos_dados_commodities():
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)  # Concatena todos os dados em um único DataFrame

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities()
    print("Dados concatenados:")
    print(dados_concatenados.head())