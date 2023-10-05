from flask import Flask, jsonify, request
import pyodbc
import pandas as pd
from flask_pydantic_spec import FlaskPydanticSpec


app = Flask(__name__ )
spec = FlaskPydanticSpec('flask', title = "Endpoints da tabela de avaliação")
spec.register(app)      

data_for_connection = (
    "Driver={SQL Server Native Client RDA 11.0};"
    "Server=DESKTOP-1698A6Q\SQLEXPRESS;"
    "Database=bncc;"  
    "Trusted_connection=YES;"
)
connection = pyodbc.connect(data_for_connection)
cursor = connection.cursor()
show_table_names = cursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES \
                                  WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='bncc'")
show_table_names = show_table_names.fetchall()

print(show_table_names)

#cursor.execute(f"drop table tabela_avaliacao")
#cursor.commit()

@app.route('/diario/notas/<turma>', methods = ["GET"])
def get_grades(turma, materia = ''):
    """Gera boletins com a nota total dos alunos de um turma, de todas as matérias ou por matéria"""    
    db_classroom = cursor.execute(f"SELECT turma from tabela_avaliacao")
    db_get_classroom = db_classroom.fetchall()
    list_c = []
    for x in db_get_classroom:
        for y in x:
            list_c.append(y)
    set_cl = set(list_c)
    print(f"""essa é a lista de turmas 
          disponíveis na escola {set_cl}""")           
    if len(materia) == 0:

        db = cursor.execute(f"""SELECT tabela_alunos.nome_completo, tabela_materias.materia,
                            tabela_alunos.turma,
                            tabela_avaliacao.total FROM tabela_alunos
                            INNER JOIN tabela_avaliacao
                            ON tabela_alunos.id_aluno = tabela_avaliacao.id_aluno 
                            INNER JOIN tabela_materias ON 
                            tabela_avaliacao.id_materia = tabela_materias.id_materia
                            where tabela_avaliacao.turma = {turma}""")
        db_get = db.fetchall()
        db_l = []
        if len(db_get) == 0:
            raise ValueError(f"""a turma {turma} solicitada não existe. 
                            As disponíveis na escola são: {set_cl}""")
        for x in db_get:
            db_l.append({
                "nome_completo": x[0],
                "materia": x[1],
                "turma": x[2],
                "total": x[3]          
                })                
        
        return jsonify(data = db_l, message = "Notas solicitadas")

           
app.run(debug=True)
    
