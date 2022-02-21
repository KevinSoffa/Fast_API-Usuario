from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return {'Ola': 'Mundo!!'}

# Criar Model
class Usuario(BaseModel):
    id: int
    email: str
    senha: str

"""class Instrumento(BaseModel):
    id: int
    nome_instrumento: str
    tipo"""

# Criar base de dados
base_de_dados = [
    Usuario(id=1, email='kevin@kevin.com', senha='123456'),
    Usuario(id=2, email='fernanda@fernanda.com', senha='fernanda123'),
    Usuario(id=3, email='leo@leo.com', senha='1234')
]

# Rota Get all
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get ID
@app.get('/usuarios/{id_usuario}')
def get_usuario_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario

    return {"Status": 404, "Mensagem":"ID não encontrado"}

# Rota Insere
@app.post('/usuarios')
def insere_usuario(usuario: Usuario):
    base_de_dados.append(usuario)
    return usuario


@app.delete('/usuarios/{id_usuario}')
def deletar_usuario(id_usuario:int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return f'Usaurio {usuario.id} DELETADO'
    return {"Status": 404, "Mensagem":"ID não encontrado"}
