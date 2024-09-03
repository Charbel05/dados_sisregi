import pymysql
import pandas as pd
import streamlit as st 
import cria_imagens as ci

connection = pymysql.connect(
    host='databasedevdb.integrator.host',
    user='samuel',
    password='Esl!FoNdZbv7ziDQ',
    db='tabelas_regulacao',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
query = '''
SELECT ta.unidade_saude_solicitante, ta.profissional, ta.procedimento, ta.solicitacoes_pendentes
FROM tabela_agenda ta
'''
try:
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    df= pd.DataFrame(results)
finally:
    connection.close()


# Dashboard usando Streamlit
st.title("Dashboard de Consultas Pendentes")
st.write("Dados coletados do SISREG III")

with st.container(height=200, border=True):
    df_selecionado = df[['solicitacoes_pendentes', 'unidade_saude_solicitante']]
    st.write(df_selecionado.sort_values('solicitacoes_pendentes', ascending=False))

# 
filtro_unidade = st.multiselect('Selecione a unidade de saúde', df['unidade_saude_solicitante'].unique())
df_filtrado = df[df['unidade_saude_solicitante'].isin(filtro_unidade)]
if len(filtro_unidade) == 0:
    df_solicitacao_medico = df[['profissional', 'solicitacoes_pendentes']]
    df_procedimento = df[['procedimento', 'solicitacoes_pendentes']]
else:
    df_solicitacao_medico = df_filtrado[['profissional', 'solicitacoes_pendentes']]
    df_solicitacao_medico = df_solicitacao_medico.groupby('profissional').sum().reset_index()
    df_procedimento = df_filtrado[['procedimento', 'solicitacoes_pendentes']]
    df_procedimento = df_procedimento.groupby('procedimento').sum().reset_index()

with st.container(height=300, border=True):
    st.altair_chart(ci.criar_grafico_horizontal(df_solicitacao_medico, 'solicitacoes_pendentes', 'profissional', 'Solicitações por Médico'))
    
with st.container(height=300, border=True):
    st.altair_chart(ci.criar_grafico_horizontal(df_procedimento, 'solicitacoes_pendentes', 'procedimento', 'Solicitações por Procedimento'))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
