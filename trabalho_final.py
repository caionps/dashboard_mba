import pandas as pd
import streamlit as st 

def load_data(path_csv: str) -> pd.DataFrame:
    with open(path_csv, 'r') as f:
        df = pd.read_csv(f)
    return df

def tab_content(df: pd.DataFrame) -> None:
    col1, col2 = st.columns(2)








df_hapvida = load_data('RECLAMEAQUI_HAPVIDA.csv')


st.title('Teste')

