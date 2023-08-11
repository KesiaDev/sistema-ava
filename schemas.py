from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    sobrenome: str
    email: str
    idade: int
    cpf: str
    id_curso: int  
    
class AlunoRequest(AlunoBase):
    ...

class AlunoResponse(AlunoBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True
