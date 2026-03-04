import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.title("Bike Sharing Dashboard")
st.markdown("Analisis Tren Penyewaan Sepeda Tahun 2011–2012")

# LOAD DATA 
@st.cache_data
def load_data():
    # Ambil lokasi file dashboard.py
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Naik satu folder lalu masuk ke data/day.csv
    data_path = os.path.join(current_dir, "..", "data", "day.csv")

    df = pd.read_csv(data_path)
    df["dteday"] = pd.to_datetime(df["dteday"])
    df["yr"] = df["yr"].map({0: 2011, 1: 2012})
    return df

df = load_data()

# VISUALISASI
st.header("Tren Penyewaan Sepeda")

yearly = df.groupby("yr")["cnt"].sum().reset_index()

fig1, ax1 = plt.subplots()
sns.barplot(data=yearly, x="yr", y="cnt", ax=ax1)
ax1.set_title("Total Penyewaan Sepeda per Tahun")
ax1.set_xlabel("Tahun")
ax1.set_ylabel("Total Penyewaan")
st.pyplot(fig1)

st.header("Pengaruh Suhu terhadap Penyewaan")

fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="temp", y="cnt", ax=ax2)
ax2.set_title("Hubungan Suhu dan Jumlah Penyewaan")
ax2.set_xlabel("Suhu")
ax2.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig2)

st.caption("Submission Dicoding - Bike Sharing Dataset")