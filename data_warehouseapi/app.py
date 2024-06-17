from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from etl.extract import buscar_todos_dados_commodities  # Ajustar o caminho conforme a estrutura

# Cria a aplicação FastAPI
app = FastAPI()

# Define o endpoint GET "/commodities/"
@app.get("/commodities/")
def get_commodities():
    """
    Endpoint para recuperar dados de commodities.

    Retorna os dados em formato JSON.
    """
    try:
        # Imprime mensagem indicando que a rota foi chamada
        print("Rota /commodities/ chamada")

        # Busca os dados de commodities
        dados_concatenados = buscar_todos_dados_commodities()

        # Imprime mensagem indicando que os dados foram obtidos
        print("Dados concatenados obtidos")

        # Converte os dados para dicionário e retorna como JSON
        return JSONResponse(content=dados_concatenados.to_dict(orient='records'))

    except Exception as e:
        # Imprime a mensagem de erro
        print(f"Erro: {e}")

        # Levanta uma exceção HTTP 500 com detalhes do erro
        raise HTTPException(status_code=500, detail=str(e))

# Ponto de entrada da aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)





