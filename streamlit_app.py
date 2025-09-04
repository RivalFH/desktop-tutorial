import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.header('Beranda!')

st.write('Hello, *Dunia!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.write('Di bawah ini adalah DataFrame:', df, 'Di atas ini adalah dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['umur', 'b', 'Ukuran'])
c = alt.Chart(df2).mark_circle().encode(
    x='umur', y='b', size='Ukuran', color='Ukuran', tooltip=['umur', 'b', 'Ukuran'])

st.write(c)