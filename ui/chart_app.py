import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'col1': [10, 12, 14, 16, 18],
    'col2': [15, 18, 20, 22, 25],
    'col3': [20, 22, 25, 28, 30]
}

df = pd.DataFrame(data)

st.write(df)

st.line_chart(df, x="year", y=['col1', 'col2', 'col3'])

st.area_chart(df, x="year", y=['col1', 'col2'])

st.bar_chart(df, x="year", y=['col1', 'col2', 'col3'])

fig, ax = plt.subplots()

ax.plot(df['year'], df['col1'], marker='o')

st.pyplot(fig)


st.divider()

plt.figure(figsize=(10,6))

for col in ['col1', 'col2', 'col3']:
    sns.lineplot(x='year', y=col, data=df, marker='o', label='col')

plt.title('Trend over Years')
plt.xlabel('Year')
plt.ylabel('Values')
st.pyplot(plt)