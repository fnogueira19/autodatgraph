import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Local File Selector")
#uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "pdf"])
uploaded_file = st.file_uploader("Choose a file", type=["csv", "dat"])

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
    st.info("Please upload a CSV file to proceed.")
