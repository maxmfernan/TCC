# - * - coding=utf8 - * -
import csv
import os
import plotly.offline as pltoff
import plotly.graph_objs as grapho

fields_name = [
    'CO_IES', 'NO_IES', 'CO_CATEGORIA_ADMINISTRATIVA', 'DS_CATEGORIA_ADMINISTRATIVA', 'CO_ORGANIZACAO_ACADEMICA', 
    'DS_ORGANIZACAO_ACADEMICA', 'CO_CURSO', 'NO_CURSO', 'CO_CURSO_POLO', 'CO_TURNO_ALUNO', 'DS_TURNO_ALUNO', 'CO_GRAU_ACADEMICO', 
    'DS_GRAU_ACADEMICO', 'CO_MODALIDADE_ENSINO', 'DS_MODALIDADE_ENSINO', 'CO_NIVEL_ACADEMICO', 'DS_NIVEL_ACADEMICO', 'CO_OCDE', 
    'NO_OCDE', 'CO_OCDE_AREA_GERAL', 'NO_OCDE_AREA_GERAL', 'CO_OCDE_AREA_ESPECIFICA', 'NO_OCDE_AREA_ESPECIFICA', 'CO_OCDE_AREA_DETALHADA', 
    'NO_OCDE_AREA_DETALHADA', 'CO_ALUNO_CURSO', 'CO_ALUNO_CURSO_ORIGEM', 'CO_ALUNO', 'CO_COR_RACA_ALUNO', 'DS_COR_RACA_ALUNO', 
    'IN_SEXO_ALUNO', 'DS_SEXO_ALUNO', 'NU_ANO_ALUNO_NASC', 'NU_MES_ALUNO_NASC', 'NU_DIA_ALUNO_NASC', 'NU_IDADE_ALUNO', 
    'CO_NACIONALIDADE_ALUNO', 'DS_NACIONALIDADE_ALUNO', 'CO_PAIS_ORIGEM_ALUNO', 'CO_UF_NASCIMENTO', 'CO_MUNICIPIO_NASCIMENTO', 
    'IN_ALUNO_DEF_TGD_SUPER', 'IN_DEF_AUDITIVA', 'IN_DEF_FISICA', 'IN_DEF_INTELECTUAL', 'IN_DEF_MULTIPLA', 'IN_DEF_SURDEZ', 
    'IN_DEF_SURDOCEGUEIRA', 'IN_DEF_BAIXA_VISAO', 'IN_DEF_CEGUEIRA', 'IN_DEF_SUPERDOTACAO', 'IN_TGD_AUTISMO_INFANTIL', 
    'IN_TGD_SINDROME_ASPERGER', 'IN_TGD_SINDROME_RETT', 'IN_TGD_TRANSTOR_DESINTEGRATIVO', 'CO_ALUNO_SITUACAO', 'DS_ALUNO_SITUACAO', 
    'DT_INGRESSO_CURSO', 'IN_ING_VESTIBULAR', 'IN_ING_ENEM', 'IN_ING_AVALIACAO_SERIADA', 'IN_ING_SELECAO_SIMPLIFICADA', 
    'IN_ING_SELECAO_VAGA_REMANESC', 'IN_ING_SELECAO_VAGA_PROG_ESPEC', 'IN_ING_TRANSF_EXOFFICIO', 'IN_ING_DECISAO_JUDICIAL', 
    'IN_ING_CONVENIO_PECG', 'IN_RESERVA_VAGAS', 'IN_RESERVA_ETNICO', 'IN_RESERVA_DEFICIENCIA', 'IN_RESERVA_ENSINO_PUBLICO', 
    'IN_RESERVA_RENDA_FAMILIAR', 'IN_RESERVA_OUTRA', 'IN_FINANC_ESTUDANTIL', 'IN_FIN_REEMB_FIES', 'IN_FIN_REEMB_ESTADUAL', 
    'IN_FIN_REEMB_MUNICIPAL', 'IN_FIN_REEMB_PROG_IES', 'IN_FIN_REEMB_ENT_EXTERNA', 'IN_FIN_REEMB_OUTRA', 'IN_FIN_NAOREEMB_PROUNI_INTEGR', 
    'IN_FIN_NAOREEMB_PROUNI_PARCIAL', 'IN_FIN_NAOREEMB_ESTADUAL', 'IN_FIN_NAOREEMB_MUNICIPAL', 'IN_FIN_NAOREEMB_PROG_IES', 
    'IN_FIN_NAOREEMB_ENT_EXTERNA', 'IN_FIN_NAOREEMB_OUTRA', 'IN_APOIO_SOCIAL', 'IN_APOIO_ALIMENTACAO', 'IN_APOIO_BOLSA_PERMANENCIA', 
    'IN_APOIO_BOLSA_TRABALHO', 'IN_APOIO_MATERIAL_DIDATICO', 'IN_APOIO_MORADIA', 'IN_APOIO_TRANSPORTE', 'IN_ATIVIDADE_EXTRACURRICULAR', 
    'IN_COMPL_ESTAGIO', 'IN_COMPL_EXTENSAO', 'IN_COMPL_MONITORIA', 'IN_COMPL_PESQUISA', 'IN_BOLSA_ESTAGIO', 'IN_BOLSA_EXTENSAO', 
    'IN_BOLSA_MONITORIA', 'IN_BOLSA_PESQUISA', 'CO_TIPO_ESCOLA_ENS_MEDIO', 'IN_ALUNO_PARFOR', 'CO_SEMESTRE_CONCLUSAO', 
    'CO_SEMESTRE_REFERENCIA', 'IN_MOBILIDADE_ACADEMICA', 'CO_MOBILIDADE_ACADEMICA', 'CO_MOBILIDADE_ACADEMICA_INTERN', 
    'CO_IES_DESTINO', 'CO_PAIS_DESTINO', 'IN_MATRICULA', 'IN_CONCLUINTE', 'IN_INGRESSO_TOTAL', 'IN_INGRESSO_VAGA_NOVA', 'ANO_INGRESSO'
]

PROCESS_DIR = os.path.dirname(os.path.abspath(__file__))
MICRODADOS_DIR = os.path.join(PROCESS_DIR, "microdados")

def main():
    fields_name_lst = [
        "students_qtd",
        'IN_DEF_AUDITIVA', 'IN_DEF_FISICA', 'IN_DEF_INTELECTUAL', 'IN_DEF_MULTIPLA', 'IN_DEF_SURDEZ',   
        'IN_DEF_SURDOCEGUEIRA', 'IN_DEF_BAIXA_VISAO', 'IN_DEF_CEGUEIRA', 'IN_DEF_SUPERDOTACAO', 'IN_TGD_AUTISMO_INFANTIL', 
        'IN_TGD_SINDROME_ASPERGER', 'IN_TGD_SINDROME_RETT', 'IN_TGD_TRANSTOR_DESINTEGRATIVO', 
        "IN_CONCLUINTE", "IN_SEXO_ALUNO",
    ]    

    fields_to_operate = [
        'IN_DEF_AUDITIVA', 'IN_DEF_FISICA', 'IN_DEF_INTELECTUAL', 'IN_DEF_MULTIPLA', 'IN_DEF_SURDEZ',   
        'IN_DEF_SURDOCEGUEIRA', 'IN_DEF_BAIXA_VISAO', 'IN_DEF_CEGUEIRA', 'IN_DEF_SUPERDOTACAO', 'IN_TGD_AUTISMO_INFANTIL', 
        'IN_TGD_SINDROME_ASPERGER', 'IN_TGD_SINDROME_RETT', 'IN_TGD_TRANSTOR_DESINTEGRATIVO', 
        "IN_CONCLUINTE", "IN_SEXO_ALUNO", 
    ]

    # DEBUG
    #getFieldNames()

    # DEBUG
    start_process(fields_to_operate)
    
    #fields_qtd = readCsv(fields_to_operate, 2)
    #doPieGraphs(fields_to_operate, fields_qtd)

def start_process(fields_to_operate):
    fields_qtd = readCsv(fields_to_operate, 2)
    doPieGraphs(fields_to_operate, fields_qtd)

# Return a list with div elements containing the bulk of informations needed to
# build graphics in a website.
def getGraphsWebComponents(fields_to_operate):
    fields_qtd = readCsv(fields_to_operate, 2)
    return doPieGraphs(fields_to_operate, fields_qtd)

# Return a list with each value in first line of the csv file.
# This first values are the fields name.
def getFieldNames():
    all_field_names = []

    with open(MICRODADOS_DIR + "/2014/DM_ALUNO.CSV", "rt", encoding="latin_1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="|")

        if( csv_reader.line_num == 0):
            all_field_names = csv_reader.__next__()
            # DEBUG
            print("DEBUG " + str(all_field_names))



    return all_field_names

# Works only for fields that have only three type of values: 0, 1 and None.
# Return a list with div elements containing the bulk of informations needed to
# build graphics in a website.
def doPieGraphs(fields_to_plot, fields_qtd):
    output_path = "../../project_site/static/graphs/"
    labels = []
    fields_value = []
    graph_objs = []
    output_div_list = []
    # Makes pie graphs for all values listed in fields_name_lst parameter.

    # Prepare graphic paramaters.
    for field in fields_to_plot:
        label = ["Não " + field, "Sim " + field, "Sem informação"]
        values = fields_qtd[field]
        #labels.append(label)
        #fields_value.append(values)
        # Set the trace that will be draw.
        graph_objs.append( grapho.Pie(labels=label, values=values) ) 
        
    with open("output_divs.txt", "wt") as output_divs:

        # Do the draw.
        for idx in range( len(fields_to_plot) ):
            output_div_list.append( pltoff.plot(
                    [graph_objs[idx]], 
                    include_plotlyjs=False, 
                    output_type="div", 
                    #filename=output_path + fields_to_plot[idx] + "_graph",
                    auto_open="False"
                ) 
            ) #/list.append
        for output_div in output_div_list:
            output_divs.write(output_div + "\n")
            print(output_div)

            return output_div_list
    ## Sex.
    #label_sex = ["Masculino", "Feminino", "Sem informação"]
    #values_sex = fields_qtd["IN_SEXO_ALUNO"]

    ## Concluinte.
    #label_concluinte = ["Não Graduando", "Graduando", "Sem informação"]
    #values_concluinte = fields_qtd["IN_CONCLUINTE"] 

    ## Deficiências.

    ## Make graphics object.
    #trace_sex = grapho.Pie(labels=label_sex, values=values_sex)
    #trace_concluinte = grapho.Pie(labels=label_concluinte, values=values_concluinte)

    ## Do the graphs.
    #pltoff.plot([trace_sex], filename="pie_sex_graph") 
    #pltoff.plot([trace_concluinte], filename="pie_concluinte_graph")
    


#def setGraphValues(field_name):
#    value_lst = []
#    for idx in range( len( fields_qtd[field_name] ) ):
#    value_lst.append(fiedls_qtd
#    return value_lst 


# Works only for fields that have only three type of values: 0, 1 and None.
def readCsv(fields_to_read, selected_course ):
    # Quantities of some type of elements.
    # Example: for IN_CONCLUINTE has the quantitie of students that graduate in the current year.
    # Works only for 3 type of values: 1, 0 and None.
    fields_qtd = {
        "students_qtd":0, 
    } 
    empty_fields_qtd = {}
    for field_name in fields_name:
        fields_qtd[field_name] = [0, 0, 0] # In order: 0 type, 1 type and none type.
        empty_fields_qtd[field_name] = 0

    csv_file = open(MICRODADOS_DIR + "/2014/DM_ALUNO.CSV", "rt", encoding="latin_1")
    #print(csv_file.readlines())
    csv_reader = csv.reader(csv_file, delimiter="|")

    # Has the name and indexs of every field in table.
    column_idxs = {}

    column_counter = 0

    # Number of rows that should be readed.
    # DBG.
    #iteration_times = 1000

    for row in csv_reader:
        # First row contains names of all fields. I want that.
        if( csv_reader.line_num == 1 ):
           for idx in range( len(row) ):
            column_idxs[row[idx]] = idx 
        #if( csv_reader.line_num == 1 ):
        #    column_names = row
        #    print(column_names)
        #    for name in row:                                
        #        column_idxs[fields_name[column_counter]] = column_counter 
        #        #if(name.endswith("_SEXO_ALUNO") ):
        #        #    column_idxs[name] = column_counter
        #        #    print(name)
        #        #elif(name.endswith("_INGRESSO_CURSO")):
        #        #    column_idxs[name] = column_counter
        #        #    print(name)
        #        
        #        column_counter += 1
        #
            print(column_idxs)
        elif( int(row[0]) == selected_course ):
        #else:
            # DBG>
            # Just to not spend to much time.
            #iteration_times -= 1
            #if(iteration_times == 0):
            #   break

            #print(row[column_idxs["DT_INGRESSO_CURSO"]])
            fields_qtd["students_qtd"] += 1


            # Read values of all fields listed in fields_to_read parameter.
            for field_n in fields_to_read:
                try:
                    if( int( row[ column_idxs[ field_n ] ] ) == 0 ):
                        fields_qtd[ field_n ][0] += 1
                    else:
                        fields_qtd[ field_n ][1] += 1
                except ValueError:
                    fields_qtd[ field_n ][2] += 1
                    
                        

            
            ## Count some variables.
            ## Add the 0's and 1's that are values of some fields. 1 is like True and 0 is like False.
            #try:
            #    if( int( row[column_idxs["IN_CONCLUINTE"]] ) == 0 ):
            #        fields_qtd["IN_CONCLUINTE"][0] += 1
            #    else:
            #        fields_qtd["IN_CONCLUINTE"][1] += 1
            #except ValueError:
            #        fields_qtd["IN_CONCLUINTE"][2] += 1

            ## 0 to masculine and 1 to feminine.
            ## Is feminine?
            #try:
            #    if( int( row[column_idxs["IN_SEXO_ALUNO"]] ) == 0 ):
            #        fields_qtd["IN_SEXO_ALUNO"][0] += 1
            #    else:
            #        fields_qtd["IN_SEXO_ALUNO"][1] += 1
            #except ValueError:
            #        fields_qtd["IN_SEXO_ALUNO"][2] += 1

            #    
            ## Some deficiencies.
            ## 1 have and 0 don't.
            #deficiencies = [
            #    'IN_DEF_AUDITIVA', 'IN_DEF_FISICA', 'IN_DEF_INTELECTUAL', 'IN_DEF_MULTIPLA', 'IN_DEF_SURDEZ',   
            #    'IN_DEF_SURDOCEGUEIRA', 'IN_DEF_BAIXA_VISAO', 'IN_DEF_CEGUEIRA', 'IN_DEF_SUPERDOTACAO', 'IN_TGD_AUTISMO_INFANTIL', 
            #    'IN_TGD_SINDROME_ASPERGER', 'IN_TGD_SINDROME_RETT', 'IN_TGD_TRANSTOR_DESINTEGRATIVO',
            #]

            #for defi in deficiencies:
            #    # Wach out! Has some value that are empty. With "".
            #    try:
            #        if( int( row[column_idxs[defi]] ) == 0):
            #            fields_qtd[defi][0] += 1
            #        else:
            #            fields_qtd[defi][1] += 1
            #    except ValueError:
            #            fields_qtd[defi][2] += 1
            #            
            #            #empty_fields_qtd[defi] += 1 

                ## DBG.
                #print(defi)
                #print(type(defi))
                #print(column_idxs[defi])
                #print(len(row[column_idxs[defi]]))
                #print(empty_fields_qtd[defi])
            
            ## DBG.
            #print(row)
        elif( int(row[0]) < selected_course ):
            continue
        else:
            break
                
                
                
                
                
                    

    # DBG.
    print("-"*10)
    print( fields_qtd )
    #print( empty_fields_qtd )
    print( fields_qtd["students_qtd"] )

    
    return fields_qtd    
            

    
   
     


if __name__ == "__main__":
    main()
