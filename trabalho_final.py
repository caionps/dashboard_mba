import pandas as pd
import streamlit as st 
from streamlit_extras.app_logo import add_logo
import plotly.express as px

# Configuração da página
st.set_page_config(layout="wide")

add_logo('logo.gif',height=400)
# add_logo('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTNiZDdwOTNudDltdnpnNngweGtmaXppb2ppOW4wbjdtM2RidnBhYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8PWAME10lhUti/giphy.gif',height=200

with st.sidebar:
    with st.container():
        st.header('Trabalho 2 - Dashboards')
        st.subheader('Aluno: Caio Nepomuceno Santos')
        st.subheader('Matrícula: 2318273')

tab1, tab2, tab3 = st.tabs(['Hapvida', 'Ibyte', 'Nagem'])

# Função para carregar os dados e fazer alterações necessárias
def load_data(path_csv: str) -> pd.DataFrame:
    with open(path_csv, 'r') as f:
        df = pd.read_csv(f)
        #df['TEMPO'] = pd.to_datetime(df['TEMPO'])
        df['UF'] = df['LOCAL'].apply(lambda x: x.split('-')[-1] if len(x.split('-')[-1]) != 2 else 'ND')
    return df

# Função para criar os gráficos nas tabs
def tab_content(df: pd.DataFrame) -> None:
    uf = st.selectbox('Selecione o estado:', index = 0, options = df['UF'].unique())
    ano = st.selectbox(label = 'Selecione o ano:', index=0, options = df['ANO'].unique())
    col1, col2 = st.columns(2)
    

    df_com_estado = df.loc[df['UF'] == uf]
    df_agrupado = df_com_estado.groupby(['ANO', 'MES'], as_index=False)['ID'].count().rename(columns={'ID': 'RECLAMAÇÕES'})
    df_agrupado_estado = df.groupby(['ANO','UF'], as_index=False)['ID'].count().rename(columns={'ID': 'RECLAMAÇÕES'})
    df_agrupado_status = df.groupby(['ANO','STATUS','UF'], as_index=False)['ID'].count().rename(columns={'ID': 'RECLAMAÇÕES'})

    
    with col1:
        st.header('Reclamações por mês')
        st.bar_chart(df_agrupado.loc[df_agrupado['ANO'] == ano], x = 'MES', y = 'RECLAMAÇÕES')
        # Aqui vai os botões de interação

    with col2:
        st.header('         .')
        st.area_chart(df_agrupado.loc[df_agrupado['ANO'] == ano], x = 'MES', y = 'RECLAMAÇÕES')


    st.header('Reclamações por estado')
    st.bar_chart(df_agrupado_estado.loc[df_agrupado_estado['ANO'] == ano], x = 'UF', y = 'RECLAMAÇÕES')
        # Aqui vai os botões de interação
        
    st.header('Status das Reclamações')
    fig = px.pie(df_agrupado_status.loc[(df_agrupado_status['ANO'] == ano) & (df_agrupado_status['UF'] == uf)], values='RECLAMAÇÕES', names='STATUS')
    st.plotly_chart(fig, use_container_width=True)

# Carregar os dados e instanciar as tabs
with tab1:
    df_hapvida = tab_content(load_data('./dados/RECLAMEAQUI_HAPVIDA.csv'))
with tab2:
    df_ibyte = tab_content(load_data('./dados/RECLAMEAQUI_IBYTE.csv'))
with tab3:
    df_nagem = tab_content(load_data('./dados/RECLAMEAQUI_NAGEM.csv'))