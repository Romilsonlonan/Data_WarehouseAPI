import time
from loguru import logger
import yfinance as yf
import pandas as pd


# Lista de commodities
commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata
# Adiciona um logger para registrar informações no arquivo "file_{time}.log"
logger.add("file_{time}.log")

# Função para buscar dados de uma única commodity
def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    """
    Busca dados históricos de uma commodity específica.

    Argumentos:
        simbolo (str): Símbolo da commodity (ex: 'CL=F' para Petróleo bruto).
        periodo (str, opcional): Período de tempo para busca (padrão: '5d' - 5 dias).
        intervalo (str, opcional): Intervalo de tempo entre os dados (padrão: '1d' - 1 dia).

    Retorna:
        DataFrame: DataFrame contendo os dados da commodity.
    """
    start_time = time.time()  # Inicia o cronômetro para medir o tempo de execução
    ticker = yf.Ticker(simbolo)  # Cria um objeto Ticker para a commodity
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]  # Obtém os dados históricos
    dados['simbolo'] = simbolo  # Adiciona a coluna 'simbolo' com o valor do símbolo
    logger.info(dados)  # Registra os dados no logger
    logger.info("--- %s seconds ---" % (time.time() - start_time))  # Registra o tempo de execução
    return dados

# Função para buscar dados de todas as commodities
def buscar_todos_dados_commodities():
    """
    Busca dados de todas as commodities da lista 'commodities'.

    Retorna:
        DataFrame: DataFrame contendo os dados concatenados de todas as commodities.
    """
    todos_dados = []  # Lista para armazenar os dados de cada commodity
    for simbolo in commodities:  # Itera sobre cada símbolo na lista
        dados = buscar_dados_commodities(simbolo)  # Busca os dados da commodity atual
        todos_dados.append(dados)  # Adiciona os dados à lista
    return pd.concat(todos_dados)  # Concatena os dados de todas as commodities em um único DataFrame

if __name__ == "__main__":
    """
    Executa quando o script é executado diretamente.
    """
    dados_concatenados = buscar_todos_dados_commodities()  # Busca os dados de todas as commodities
    print("Dados concatenados:")  # Imprime o título da seção
    print(dados_concatenados.head())  # Imprime as primeiras linhas do DataFrame
