from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from etl.extract import buscar_todos_dados_commodities  # Ajustar o caminho conforme a estrutura

app = FastAPI()

@app.get("/commodities/")
def get_commodities():
    try:
        dados_concatenados = buscar_todos_dados_commodities()
        print("Rota /commodities/ chamada")
        dados_concatenados = buscar_todos_dados_commodities()
        print("Dados concatenados obtidos")
        return JSONResponse(content=dados_concatenados.to_dict(orient='records'))  # Converte para dicionário e retorna como JSON
    except Exception as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)




