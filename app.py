import streamlit as st

st.title("タイトル")

st.write("これは基本的なStreamlitアプリです。")

st.header("ヘッダー")
st.subheader("サブヘッダー")
st.text("通常のテキスト")
st.markdown("**Markdown** を使うこともできます。")



import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)

st.dataframe(df)  # インタラクティブなテーブル
st.table(df.head())  # 静的なテーブル

import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
