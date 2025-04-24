from fastapi import FastAPI
from fastapi.responses import JSONResponse
import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="senha123",
    port="5432"
)

cursor = conexao.cursor()


app = FastAPI()

@app.get("/")
def read_root():
    return{"menssage":"Api funcionando"}

@app.get("/usuario/{usuario_id}")
def read_user(usuario_id: int):
    cursor.execute("SELECT * FROM users WHERE id = %s", (usuario_id,))
    resultado = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]

    resultado_json = [dict(zip(colunas, linha)) for linha in resultado]

    return JSONResponse(content=resultado_json)

    # return {"Usuário Id": usuario_id}

@app.get("/usuarios")
def read_all_users():
    cursor.execute("SELECT * FROM users")
    resultado = cursor.fetchall() #Resgata o valor dos dados, puros

    colunas = [desc[0] for desc in cursor.description] #Pega o indice de cada coluna "id", "name", "email"

    resultado_json = [dict(zip(colunas, linha)) for linha in resultado] #Transformas a lista de tuplas (fornecidas pela variavel  resultado) em uma lista de dicionários
    return JSONResponse(content=resultado_json) #Retorna um json





