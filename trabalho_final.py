import pandas as pd
import streamlit as st 
from streamlit_extras.app_logo import add_logo

# Configuração da página
st.set_page_config(layout="wide")

add_logo('logo.gif',height=400)
# add_logo('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTNiZDdwOTNudDltdnpnNngweGtmaXppb2ppOW4wbjdtM2RidnBhYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8PWAME10lhUti/giphy.gif',height=200

with st.sidebar:
    with st.container():
        st.header('Trabalho 2 - Dashboards')
        st.subheader('Aluno: Caio Nepomuceno Santos')
        st.subheader('Matrícula: 2318273')

tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

def load_data(path_csv: str) -> pd.DataFrame:
    with open(path_csv, 'r') as f:
        df = pd.read_csv(f)
    return df

def tab_content(df: pd.DataFrame) -> None:
    col1, col2 = st.columns(2)

    with col1:
        st.line_chart(df, x = 'ID', y = 'CASOS')
        # Aqui vai os botões de interação

    with col2:
        st.bar_chart(df, x = 'ID', y = 'CASOS')
        # Aqui vai os botões de interação

    col3, col4 = st.columns(2)

    with col3:
        st.area_chart(df, x = 'ID', y = 'CASOS')
    
    with col4:
        st.altair_chart(df, use_container_width=True)



# Carregar os dados e instanciar as tabs
with tab1:
    df_hapvida = tab_content(load_data('./dados/RECLAMEAQUI_HAPVIDA.csv'))
with tab2:
    df_ibyte = tab_content(load_data('./dados/RECLAMEAQUI_IBYTE.csv'))
with tab3:
    df_nagem = tab_content(load_data('./dados/RECLAMEAQUI_NAGEM.csv'))