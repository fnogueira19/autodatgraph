import pandas as pd
import streamlit as st
#import streamlit.components.v1 as components
import plotly.express as px

st.title("Selecione o arquivo .dat")
#uploaded_file = st.file_uploader("Escolha o arquivo", type=["csv", "dat"])
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)
uploaded_file = st.file_uploader('Arraste e solte o arquivo DAT ou clique para selecionar', type=["csv", "dat"])

if uploaded_file is not None:

    df1 = pd.read_csv(uploaded_file, skiprows = 1)
    df2 = df1.drop('RECORD', axis=1)

    df_filtered = df2[df2['TIMESTAMP'].str.contains('01:00|05:00|09:00|13:00|17:00|21:00')]
    df_filtered = df_filtered.set_index('TIMESTAMP')

    for coluna in df_filtered.columns:
        fig = px.line(df_filtered, y=coluna, height=250)

        num_coluna = df_filtered.columns.get_loc(coluna)
        if num_coluna % 2 != 0:
            fig.update_traces(line_color = 'red')
            fig.update_layout(xaxis_title='')
        else:
            fig.update_traces(line_color = 'blue')
            fig.update_layout(xaxis_title='')
        st.plotly_chart(fig)

else:
    st.info("Favor carregar arquivo .dat válido")
