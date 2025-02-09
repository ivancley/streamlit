import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboad", page_icon="📊", layout="wide")

pd.options.display.float_format = lambda x: f"{x:,.0f}".replace(",", ".") 
df = pd.read_csv('alunos_cursos.csv')
df['idade_aluno'] = df['idade_aluno'].astype(int)
df['data_matricula'] = pd.to_datetime(df['data_matricula'], format='%d/%m/%Y')
df['concluiu_curso'] = df['concluiu_curso'].astype(bool)
df['ano_matricula'] = df['data_matricula'].dt.year


# Esconder Menu padrão
hide_settings_menu = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_settings_menu, unsafe_allow_html=True)


# Filtros 
nome = ""
try:
    nome = st.query_params["nome"]
except: 
    nome = ""

if nome not in [""]: 
    df = df[df['professor'] == nome]
    st.write(f'Olá, {st.query_params["nome"]}!')
    
else:
    l0_col1, l0_col2 = st.columns(2)

    escolas = df['escola_aluno'].value_counts().index 
    with l0_col1:
        escola = st.selectbox("Escolas", escolas, index=None, placeholder="Escolha uma escola")
        if escola in escolas:
            df = df[df['escola_aluno'] == escola]

    professores = df['professor'].value_counts().index
    with l0_col2:
        professor = st.selectbox("Professores", professores, index=None, placeholder="Escolha um professor")
        if professor in professores:
            df = df[df['professor'] == professor]

    st.divider()

alunos_por_sexo = df['sexo_aluno'].value_counts()
alunos_por_idade = df['idade_aluno'].value_counts()
alunos_por_escolaridade = df['escolaridade_aluno'].value_counts()
df_concluidos = df[df['concluiu_curso'] == True]
alunos_concluidos_por_ano = df_concluidos.groupby('ano_matricula')['nome_aluno'].agg('count')

l1_col1, l1_col2, l1_col3, l1_col4 = st.columns(4)
with l1_col1:
    st.write('Sexo')
    l1_col1.bar_chart(alunos_por_sexo, horizontal=False)

with l1_col2:
    st.write('Idade')
    l1_col2.bar_chart(alunos_por_idade, horizontal=False, x_label='Idade')
    
with l1_col3:
    st.write('Escolaridade - Ensino Médio')
    l1_col3.bar_chart(alunos_por_escolaridade, horizontal=False)
    
with l1_col4:
    st.write('Concludidos por ano')
    l1_col4.bar_chart(alunos_concluidos_por_ano, horizontal=False)


l2_col1, l2_col2, l2_col3 = st.columns(3)

df_filter_cursos_concluidos = df[df['concluiu_curso'] == True]
df_cursos_concluidos = df_filter_cursos_concluidos.groupby('curso')['nome_aluno'].agg('count')
df_cursos_concluidos = df_cursos_concluidos.sort_values(ascending=True)

df_media_notas_curso = df.groupby('curso')['respostas_corretas'].agg('mean')

df_media_notas_curso_alunos = df.groupby('curso')['avaliacao_curso'].agg('mean')

with l2_col1:
    st.write('Cursos mais concluidos')
    l2_col1.bar_chart(df_cursos_concluidos, horizontal=True)

with l2_col2:
    st.write('Cursos por média')
    l2_col2.bar_chart(df_media_notas_curso, horizontal=True)
    
with l2_col3:
    st.write('Cursos por média')
    l2_col3.bar_chart(df_media_notas_curso_alunos, horizontal=True)
    
df_aluno = df[['sexo_aluno', 'idade_aluno', 'escola_aluno', 'curso', 'avaliacao_curso']]


st.dataframe(df_aluno, use_container_width=True)