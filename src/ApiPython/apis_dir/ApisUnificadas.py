from flask import Flask, jsonify, request
import pyodbc
import pandas as pd
from flask_pydantic_spec import FlaskPydanticSpec
from datetime import datetime
from dateutil.parser import parse


app = Flask(__name__ )
spec = FlaskPydanticSpec(title = "Endpoints da tabela de avaliação", \
    description = "Documentação da api")
spec.register(app)

app.config['id_for_grades'] = None

#Notebook
# data_for_connection = (
#     "Driver={SQL Server};"
#     "Server=DESKTOP-O0ICHS5;"
#     "Database=BancoDiario_Atualizado;"  
#     "Trusted_connection=YES;"
# )

#Desktop
data_for_connection = (
  "Driver={SQL Server Native Client RDA 11.0};"
    "Server=DESKTOP-JKC28N9\SQLEXPRESS;"
    "Database=BancoDiario_Atualizado;"  
    "Trusted_connection=YES;"
)

connection = pyodbc.connect(data_for_connection)
cursor = connection.cursor()


# cursor.execute(f"""
#                    create table tabela_atividade (
#                 id_aluno int,                
#                    id_materia int, 
#                    id_bimestre int, 
#                    id_avaliacao int, 
#                    descricao_at nvarchar(100),
#                    codigo_atividade int,
#                    turma int)""")


# cursor.execute(f"""insert into tabela_atividade 
#                (id_avaliacao, id_materia, id_bimestre,
#                descricao_at, codigo_atividade, turma) 
#                select id_aluno, id_avaliacao, id_materia, id_bimestre,
#                descricao_at, codigo_atividade, turma from 
#                tabela_avaliacao""")
cursor.commit()

#funcionando
@app.route('/diario/atividades', methods = ['GET'])
def get_all_act():
    """Lista todas as atividades de todos os alunos de todas as turmas"""

    db = cursor.execute(f"""SELECT a.*, b.bimestre, c.materia
                            FROM tabela_atividade AS a
                            INNER JOIN tabela_bimestre AS b ON a.id_bimestre = b.id_bimestre 
                            INNER JOIN tabela_materias AS c ON a.id_materia = c.id_materia       
                        """)
    db = db.fetchall()
    db_l = []
    for x in db:
        db_l.append({
            'id_materia': x[0],
            'id_bimestre': x[1],
            'descricao_at': x[2],
            'turma': x[3],
            'id_atividade': x[4],
            'atv_status': x[5],
            'data_cadastro_atv': x[6],
            'bimestre': x[7],
            'materia': x[8]
        })
    return jsonify(message = "Todas as atividades", lista_total = db_l)

#testando mudei aqui
@app.route('/diario/atividade/<int:id_atividade>', methods = ['GET'])
def get_act_by_id(id_atividade):
    db = cursor.execute(f"""SELECT a.*, b.bimestre, c.materia
                            FROM tabela_atividade AS a
                            INNER JOIN tabela_bimestre AS b ON a.id_bimestre = b.id_bimestre 
                            INNER JOIN tabela_materias AS c ON a.id_materia = c.id_materia    
                            WHERE a.id_atividade = {id_atividade}
                       """)
    query_data = db.fetchone() 
    
    if query_data is not None:
        db = {
            'id_materia': query_data[0],
            'id_bimestre': query_data[1],
            'descricao_at': query_data[2],
            'turma': query_data[3],
            'id_atividade': query_data[4],
            'atv_status': query_data[5],
            'data_cadastro_atv': query_data[6],
            'bimestre': query_data[7],
            'materia': query_data[8]
    }
    return jsonify(message = f"Alunos da atividade listados", data = db)
    
    
#=================API ATIVIDADE=======================
#=======================Tirei do query string passei pro body
@app.route('/diario/inserir/atividades', methods=['POST'])
def insert_act():
    """Insere uma nova atividade"""
    
    act_obj = request.get_json(force=True)
    
    id_materia = act_obj.get('id_materia')
    id_bimestre = act_obj.get('id_bimestre')
    turma = act_obj.get('turma')
    act_des = act_obj.get('descricao_at')
    
    if id_materia is None or id_bimestre is None or turma is None:
        return jsonify(message="Certifique-se de fornecer id_materia, id_bimestre e turma no corpo da solicitação."), 400
    
    data_hora_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute(f"""INSERT INTO tabela_atividade (id_materia, id_bimestre, turma, descricao_at, atv_status, data_cadastro_atv)
                   VALUES ({id_materia}, {id_bimestre}, {turma}, '{act_des}', 0, '{data_hora_at}')""")
    
    cursor.execute("SELECT SCOPE_IDENTITY() AS last_insert_id")
    last_id_act = cursor.fetchone().last_insert_id
    
    act_obj.update({'id_atividade': last_id_act})
    
    cursor.commit()
    
    return jsonify(message=f"Atividade inserida com sucesso e o id inserido é {last_id_act}", data=act_obj)

@app.route('/diario/atualizar/<int:id_atividade>', methods=['PUT'])
def update_act(id_atividade):
    """atualiza uma atividade"""
    
    act_obj = request.get_json(force=True)
    
    id_materia = act_obj.get('id_materia')
    id_bimestre = act_obj.get('id_bimestre')
    turma = act_obj.get('turma')
    act_des = act_obj.get('descricao_at')    
    
    cursor.execute(f"""UPDATE tabela_atividade SET 
                   id_bimestre = {id_bimestre}, 
                   turma = {turma}, 
                   descricao_at = '{act_des}',
                   id_materia = {id_materia}
                   WHERE id_atividade = {id_atividade}
                   """)
    
    
    act_obj.update({'id_atividade': id_atividade})
    
    cursor.commit()
    
    return jsonify(message=f"Atividade inserida com sucesso e o id inserido é {id_atividade}", data=act_obj)

@app.route('/diario/atualizar/status/<int:id_atividade>', methods=['PUT'])
def update_act_status(id_atividade):
    """Atualiza o status de uma atividade"""

    status = request.get_json(force=True).get('atv_status')

    cursor.execute(f"""UPDATE tabela_atividade
                   SET atv_status = '{status}'
                   WHERE id_atividade = {id_atividade}
                   """)

    cursor.commit()

    return jsonify(message=f"Status da atividade com ID {id_atividade} atualizado com sucesso para '{status}'")

#==========================criei um insert para a tabela avaliaçoes ele insere cada uma das notas o foreach é feito no front
@app.route('/diario/inserir/nota', methods=['POST'])
def insert_nota():
    """Insere uma nova nota"""
    
    act_obj = request.get_json(force=True)
    
    id_aluno = act_obj.get('id_aluno')
    id_materia = act_obj.get('id_materia')
    id_bimestre = act_obj.get('id_bimestre')
    nota = act_obj.get('nota_5')
    total = act_obj.get('total')
    id_atividade = act_obj.get('id_atividade')
    
    cursor.execute(f"""INSERT INTO tabela_avaliacao (id_materia, id_bimestre, id_aluno, id_atividade, nota_5, total)
                   VALUES ({id_materia}, {id_bimestre}, {id_aluno}, {id_atividade}, {nota}, {total})""")
    
    cursor.commit()
    
    return jsonify(message=f"Avaliacao inserida com sucesso ", data=act_obj)
#==========================criei endpoint para listar todas as avaliações
@app.route('/diario/avaliacao', methods = ['GET'])
def get_all_av():
    """Lista TODAS AS AVALIACOES DA ATIVIDADE"""

    db = cursor.execute(f"""SELECT *
                            FROM tabela_avaliacao                          
                        """)
    db = db.fetchall()
    db_l = []
    for x in db:
        db_l.append({
            'id_aluno':x[0],
            'id_materia': x[1],
            'id_bimestre': x[2],
            'nota_1':x[3],
            'nota_2': x[4],
            'nota_3': x[5],
            'nota_4': x[6],
            'nota_5': x[7],
            'total': x[8],
            'id_avaliacao':x[9],
            'id_atividade':x[10]
        })
    return jsonify(message = "Todas as avaliacoes2222", lista_total = db_l)

#==========================mudei o endpoint para /aluno listar por aluno
@app.route('/diario/avaliacao/aluno/<int:id_aluno>', methods = ['GET'])
def get_by_id_aln(id_aluno):
    """Lista TODAS AS AVALIACOES DA ATIVIDADE"""

    db = cursor.execute(f"""SELECT *
                            FROM tabela_avaliacao
                            WHERE id_aluno = {id_aluno}                          
                        """)
    db = db.fetchall()
    db_l = []
    for x in db:
        db_l.append({
            'id_aluno':x[0],
            'id_materia': x[1],
            'id_bimestre': x[2],
            'nota_1':x[3],
            'nota_2': x[4],
            'nota_3': x[5],
            'nota_4': x[6],
            'nota_5': x[7],
            'total': x[8],
            'id_avaliacao':x[9],
            'id_atividade':x[10]
        })
    return jsonify(message = "Todas as avaliacoes2222", lista_total = db_l)
        
#==========================mudei o endpoint para /atividade listar por atividade
@app.route('/diario/avaliacao/atividade/<int:id_atividade>', methods = ['GET'])
def get_by_id_atv(id_atividade):
    """Lista TODAS AS AVALIACOES DA ATIVIDADE"""

    db = cursor.execute(f"""SELECT *
                            FROM tabela_avaliacao
                            WHERE id_atividade = {id_atividade}                          
                        """)
    db = db.fetchall()
    db_l = []
    for x in db:
        db_l.append({
            'id_aluno':x[0],
            'id_materia': x[1],
            'id_bimestre': x[2],
            'nota_1':x[3],
            'nota_2': x[4],
            'nota_3': x[5],
            'nota_4': x[6],
            'nota_5': x[7],
            'total': x[8],
            'id_avaliacao':x[9],
            'id_atividade':x[10]
        })
    return jsonify(message = "Todas as avaliacoes", lista_total = db_l)
               
#========================API ATIVIDADE FIM =========================


#======================API ALUNOS ===================================
@app.route('/diario/inserir', methods = ['POST'])
def insert_student():
    """Insere um novo estudante"""
    
    new_std = request.get_json(force=True)
    new_na = new_std['nome']
    new_su = new_std['sobrenome']
    new_fn = new_std['nome'] + ' ' + new_std['sobrenome']
    new_gr = new_std['ano']
    new_l = new_std['nivel_ensino']
    new_ag = new_std['idade']
    new_c = new_std['cpf']
    new_cl = new_std['turma']
    data_hora_aln = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute(f""" INSERT INTO tabela_alunos (nome, sobrenome, nome_completo,
                   ano, nivel_ensino, idade, cpf, turma, status_aluno, data_cadastro_aln)
                   VALUES ('{new_na}', '{new_su}', '{new_fn}', '{new_gr}',
                   '{new_l}', {new_ag},
                   '{new_c}', {new_cl}, 'true', '{data_hora_aln}')
                   """)
    cursor.execute(f"SELECT SCOPE_IDENTITY() AS last_insert_id")
    last_id = cursor.fetchone().last_insert_id
    print(f"o último id inserido foi o {last_id}")
    new_std.update({'id_aluno': last_id})
    cursor.commit()
    return jsonify(message = f"Aluno * {str.upper(new_fn)} * id {last_id}, cadastrado com sucesso", data = new_std)

@app.route('/diario/deletar/<id_student>/<status_aluno>', methods = ['PUT'])
def delete_student(id_student, status_aluno):

    """Altera status do estudante"""    
    cursor.execute(f"""UPDATE tabela_alunos SET status_aluno = {status_aluno}
                    WHERE id_aluno ={id_student}
                """)
    cursor.commit()
    response_data = {"id_aluno": id_student}
    return jsonify(message = "Aluno deletado da lista. ", data=response_data)    
    
    
@app.route('/diario/atualizar/aluno/<id_student>', methods = ['PUT'])
def update_std(id_student):
    """Atualiza um estudante da lista"""  
    updated_data = request.get_json(force=True)
    up_na = updated_data['nome']
    up_su = updated_data['sobrenome']
    up_fn =updated_data['nome'] + updated_data['sobrenome']
    up_gr = updated_data['ano']
    up_le = updated_data['nivel_ensino']
    up_ag = updated_data['idade']
    up_cpf = updated_data['cpf']
    up_cl = updated_data['turma']
    
    cursor.execute(f"""UPDATE tabela_alunos SET nome = '{up_na}', 
                   sobrenome = '{up_su}', nome_completo = '{up_fn}',
                   ano = '{up_gr}', nivel_ensino = '{up_le}', 
                   idade = {up_ag}, cpf = '{up_cpf}', turma = {up_cl}
                   WHERE id_aluno ={id_student}
                   """)
    
    cursor.commit()
    updated_data.update({'id_aluno': id_student})
    return(jsonify(message = f"Estudante {up_fn} atualizado", data=updated_data))
    

@app.route('/diario', methods = ['GET'])
#@spec.validate(resp=Response(HTTP_200=Student))
def list_all_students():
    """Lista todos os estudantes da escola """
    db = cursor.execute(f"SELECT * FROM tabela_alunos ORDER BY id_aluno DESC")
    query_st = db.fetchall()
    all_st = []
    for x in query_st:
        all_st.append({
            "nome": x[0],
            "sobrenome": x[1],
            "nome_completo": x[2],
            "ano": x[3],
            "nivel_ensino": x[4],
            "idade": x[5], 
            "cpf": x[6],
            "turma": x[7],
            "id_aluno" : x[8],
            "status_aluno": x[9],
            "data_cadastro_aln": x[10],
            


        })
    return jsonify(message = "Lista de todos os alunos", lista_total = all_st)

@app.route('/diario/aluno/<id_student>', methods=['GET'])
def list_student_by_id(id_student):
    "Lista os dados de um estudante pelo id"
    db = cursor.execute("SELECT * FROM tabela_alunos where id_aluno = ?", (id_student,))
    query_data = db.fetchone()  # Use fetchone() to retrieve a single row

    if query_data is not None:
        student_data = {
            "nome": query_data[0],
            "sobrenome": query_data[1],
            "nome_completo": query_data[2],
            "ano": query_data[3],
            "nivel_ensino": query_data[4],
            "idade": query_data[5],
            "cpf": query_data[6],
            "turma": query_data[7],
            "id_aluno": query_data[8],
            "status_aluno": query_data[9],
            "data_cadastro_aln": query_data[10]
        }
        return jsonify(data=student_data, message="Aluno solicitado")
    else:
        return jsonify(message="Aluno não encontrado"), 404 
#==================================API ALUNOS FIM======================================
 
 #===================================API Aula======================================
@app.route('/diario/aula/registrar', methods = ['POST'])
def insert_class():
    obj_cla = request.get_json(force=True)
    id_materia = obj_cla.get('id_materia')
    id_bimestre = obj_cla.get('id_bimestre')
    data_aula = parse(obj_cla.get('data_aula'))
    descricao_aula = obj_cla.get('descricao_aula')
    habilidade_bncc = obj_cla.get('habilidade_bncc')
    id_turma = obj_cla.get('id_turma')
    ano = obj_cla.get('ano')
    
    cursor.execute(f"""INSERT INTO tabela_aulas (id_materia, id_bimestre, data_aula, 
                   descricao_aula, habilidade_bncc, id_turma, ano) VALUES ({id_materia}, 
                   {id_bimestre}, '{data_aula}', '{descricao_aula}', '{habilidade_bncc}', {id_turma}, '{ano}')
                   """)
    cursor.execute(f"SELECT SCOPE_IDENTITY() AS last_insert_id")
    id_aula = cursor.fetchone().last_insert_id
    obj_cla.update({'id_aula': id_aula})
    cursor.commit()
    
    return jsonify(data = obj_cla, message = "Aula inserida com sucesso")

@app.route('/diario/aula/atualizar/<int:id_aula>', methods=['PUT'])
def update_class(id_aula):
    obj_cla = request.get_json(force=True)
    id_materia = obj_cla.get('id_materia')
    id_bimestre = obj_cla.get('id_bimestre')
    data_aula = parse(obj_cla.get('data_aula'))
    descricao_aula = obj_cla.get('descricao_aula')
    habilidade_bncc = obj_cla.get('habilidade_bncc')
    id_turma = obj_cla.get('id_turma')
    ano = obj_cla.get('ano')

    cursor.execute(f"""
        UPDATE tabela_aulas 
        SET id_materia = {id_materia}, 
            id_bimestre = {id_bimestre}, 
            data_aula = '{data_aula}', 
            descricao_aula = '{descricao_aula}', 
            habilidade_bncc = '{habilidade_bncc}', 
            id_turma = {id_turma}, 
            ano = '{ano}'
        WHERE id_aula = {id_aula}
    """)
    
    obj_cla.update({'id_aula': id_aula})
    cursor.commit()

    return jsonify(data=obj_cla, message=f"Aula com ID {id_aula} atualizada com sucesso")
    

@app.route('/diario/aula/listar/', methods=['GET'])
def get_all_classes():
    db = cursor.execute(f"""SELECT a.*, b.bimestre, c.materia
                            FROM tabela_aulas AS a
                            INNER JOIN tabela_bimestre AS b ON a.id_bimestre = b.id_bimestre 
                            INNER JOIN tabela_materias AS c ON a.id_materia = c.id_materia """)
    db_list = db.fetchall()
    aulas = []

    for aula in db_list:
        aulas.append({
            "id_aula": aula[0],
            "id_materia": aula[1],
            "id_bimestre": aula[2],
            "data_aula": aula[3],
            "descricao_aula": aula[4],
            "habilidade_bncc": aula[5],
            "id_turma": aula[6],
            "ano": aula[7],
            "bimestre": aula[8],
            "materia": aula[9]
        })

    return jsonify(listar_total=aulas, message="Todas as aulas retornadas")

@app.route('/diario/aula/<int:id_aula>', methods=['GET'])
def get_class_by_id(id_aula):
    db = cursor.execute(f"""SELECT a.*, b.bimestre, c.materia
                            FROM tabela_aulas AS a
                            INNER JOIN tabela_bimestre AS b ON a.id_bimestre = b.id_bimestre 
                            INNER JOIN tabela_materias AS c ON a.id_materia = c.id_materia  
                            WHERE id_aula = {id_aula}""")
    db_data = db.fetchone()

    if db_data is not None:
        aula_data = {
            "id_aula": db_data[0],
            "id_materia": db_data[1],
            "id_bimestre": db_data[2],
            "data_aula": db_data[3],
            "descricao_aula": db_data[4],
            "habilidade_bncc": db_data[5],
            "id_turma": db_data[6],
            "ano": db_data[7],
            "bimestre": db_data[8],
            "materia": db_data[9]
        }

        return jsonify(data=aula_data, message="Todas as aulas retornadas")
    else:
        return jsonify(message="Aula não encontrada"), 404
    
    
    
#===================================API Aula FIM======================================
 
 
 #==================================API Frequencia =====================================
 
# @app.route('/diario/frequencia/inserir', methods = ["POST"])
# def insert_freq():
#     """insere presença para todos de uma turma"""
#     payload = request.get_json(force=True)
#     id_aula = payload.get('id_aula')
#     presente = payload.get('presente')
#     db_turma = cursor.execute(f"SELECT id_turma from tabela_aulas WHERE id_aula = {id_aula}")
#     db_turma = db_turma.fetchall()
#     id_turma = db_turma[0][0]
#     db_ids = cursor.execute(f"""SELECT id_aluno FROM tabela_alunos WHERE id_turma = {id_turma}""")
#     list_ids = db_ids.fetchall()
#     dic_ids = []
#     for x in list_ids:
#         for y in x:
#             dic_ids.append({
#                 "id_aluno": y
#             })
#     print(f"esses são os alunos  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% {dic_ids}")
#     result = []
    
#     id_alunos_adicionados = set()
    
#     for id_aluno in dic_ids:
#         if id_aluno["id_aluno"] not in id_alunos_adicionados:
#             result.append({
#                 "id_aluno": id_aluno["id_aluno"],
#                 "id_aula": id_aula,
#                 "presente": presente  
#             })
#             id_alunos_adicionados.add(id_aluno["id_aluno"])    
 
#     print(f"esse é o result final %%%%%%%%%%$$$$$$$$$$$$$$$$$$$$$$$$$$$$ {result}")   
#     id_freq_list = []
#     for x in result:
#         cursor.execute(f"""INSERT INTO tabela_frequencia (id_aluno, id_aula, presente) VALUES (
#                            {x['id_aluno']}, {x['id_aula']}, {x['presente']}       
#                        ) """)
#         cursor.commit()
#         cursor.execute(f"SELECT SCOPE_IDENTITY() AS last_insert_id")
#         id_freq = cursor.fetchone().last_insert_id
#         id_freq_list.append(id_freq)
#     id_freq_f = []
#     for x in id_freq_list:
#         id_freq_f.append({
#             "id_frequencia": int(x)
#         })        
#     for i, x in enumerate(result):
#         x['id_frequencia'] = id_freq_f[i]['id_frequencia']
#         print(f"printando a chave i {i} printando o valor x {x}")       
        
    
#     return jsonify(message= "está funcionando", data = result) 
    
@app.route('/diario/frequencia/listar/', methods = ['GET'])
def get_frequency_by_idAula():
    id_aula = request.values.get('id_aula')
    db = cursor.execute(f"""SELECT * FROM tabela_frequencia where id_aula = {id_aula}""")
    db = db.fetchall()
    db_list = []
    for x in db:
        db_list.append(
            {
                "id_aluno": x[0],
                "presente": x[1],
                "id_frequencia": x[2],
                "id_aula": x[3]
            }
        )
    return jsonify(lista_total = db_list, message = f"Listagem de frequência da aula de id = {id_aula}")

@app.route('/diario/frequencia/listarTodos/', methods=['GET'])
def get_frequency_all():
    
    cursor.execute("SELECT * FROM tabela_frequencia")
    db = cursor.fetchall()
    db_list = []

    for x in db:
        db_list.append({
            "id_aluno": x[0],
            "presente": x[1],
            "id_frequencia": x[2],
            "id_aula": x[3],
        })

    # Retorne os resultados como JSON
    return jsonify(lista_total=db_list, message="Listagem de frequência da aula por id")

@app.route('/diario/frequencia/deletar/', methods = ['DELETE'])
def delete_frequency():
    id_aula = request.values.get('id_aula')
    cursor.execute(f"""
                   DELETE FROM tabela_frequencia WHERE id_aula = {id_aula}
                   """)
    cursor.commit()


@app.route('/diario/frequencia/atualizar/<int:id_frequencia>', methods=['PUT'])
def update_frequency(id_frequencia):
    up_obj = request.get_json(force=True)
    up_presente = up_obj.get('presente')
    
    cursor.execute(f"""UPDATE tabela_frequencia SET presente = '{up_presente}'
                       WHERE id_frequencia = {id_frequencia}
                    """)
    
    up_obj.update({'id_frequencia': id_frequencia})
    cursor.commit()    
    
    return jsonify(message="Tabela frequência atualizada", data=up_obj)
  
   

@app.route('/diario/frequencia/inserir', methods = ["POST"])
def insert_freq():
    act_obj = request.get_json(force=True)

    id_aluno = act_obj.get('id_aluno')
    id_aula = act_obj.get('id_aula')
    presente = act_obj.get('presente')
    
    cursor.execute(f"""INSERT INTO tabela_frequencia (id_aluno,  id_aula, presente)
                   VALUES ({id_aluno}, {id_aula}, '{presente}')""")
    
    
    cursor.execute("SELECT SCOPE_IDENTITY() AS last_insert_id")
    last_id_fq = cursor.fetchone().last_insert_id
    
    act_obj.update({'id_frequencia': last_id_fq})
    cursor.commit()
    
    return jsonify(message=f"Frequencia inserida com sucesso ", data=act_obj) 



#===================================API Frequencia FIM======================================== 
 

#===================================API BNCC================================================
 
@app.route('/apibncc/habilidades/', methods = ["GET"])
def list_all_three():
    """Lista todo as habilidades por matéria e ano via query string"""
    subject = request.args.get('materia', None, type= str)
    grade = request.args.get('ano', None, type = str)
                          
    
    if len(grade) > 0 and len(subject) > 0:      
        db = cursor.execute(f"""SELECT habilidades
                                FROM {subject} where {grade} = 'true'""")
        data_get = db.fetchall()
        data_show = []
        if subject == "bncc_lingua_portuguesa_ef":
            pl_list = []
            for x in data_get:
                pl_list.append({
                'habilidades': x[0],
            })
            return jsonify(message = "Dados solicitados", data = pl_list)
        elif subject == "bncc_lingua_inglesa_ef":
            eng_list = []
            for x in data_get:
                eng_list.append({
                    'habilidades': x[0]
            
            })
            return jsonify(message = "dados", data = eng_list)
        elif subject.endswith("_ef") and subject not in ["bncc_lingua_portuguesa_ef", "bncc_lingua_inglesa_ef"]:
            for x in data_get:
                data_show.append({                   
        'habilidades': x[0]
                
            })
            return jsonify(message= "dados", data = data_show)
        
        elif subject.endswith("_em") and not subject.startswith("c"):
            em_list = []
            db = cursor.execute(f"""SELECT habilidades
                            FROM {subject} where {grade} = 'true'""")
            for x in data_get:
                em_list.append({                   
                  'habilidades': x[0]
                })
            return jsonify(message = "Dados de df_habilidades_em", data = em_list)
        elif subject.endswith("_em") and subject.startswith("c"):
            em_competencias_list = []
            db = cursor.execute(f"""SELECT habilidades
                            FROM {subject} where {grade} = 'true'""")
            for x in data_get:
                em_competencias_list.append({
                  'habilidades': x[0]
                })
            return jsonify(message = "Dados solicitados", data = em_competencias_list)
 #===================================API BNCC FIM================================================
 
               
app.run(debug=True)