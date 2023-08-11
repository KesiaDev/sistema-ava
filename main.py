from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Curso, Aluno  
from database import engine, Base, get_db
from repositories import CursoRepository, AlunoRepository  # Importe os repositórios de Curso e Aluno
from schemas import CursoRequest, CursoResponse, AlunoRequest, AlunoResponse  # Importe os schemas necessários

Base.metadata.create_all(bind=engine)

app = FastAPI()




@app.post("/api/alunos", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def create_aluno(request: AlunoRequest, db: Session = Depends(get_db)):
    aluno = AlunoRepository.save(db, Aluno(**request.dict()))
    return AlunoResponse.from_orm(aluno)

@app.get("/api/alunos", response_model=list[AlunoResponse])
def find_all_alunos(db: Session = Depends(get_db)):
    alunos = AlunoRepository.find_all(db)
    return [AlunoResponse.from_orm(aluno) for aluno in alunos]



def custom_openapi():

    pass

app.openapi = custom_openapi
