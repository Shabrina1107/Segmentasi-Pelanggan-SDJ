import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("Segmentasi Pelanggan Sesuatu di Jogja")

# Deskripsi
st.write("""Peneliti melakukan segmentasi pelanggan untuk membantu SDJ dalam memahami karakter pelanggan secara personal untuk meningkatkan loyalitas pelanggan 
""")

# Fungsi untuk membaca data dari file
@st.cache_data
def load_data(file_path):
    # Anda dapat mengganti ini dengan fungsi pembacaan data sesuai kebutuhan
    return pd.read_csv(file_path)

# Memuat data
data_path = './data_skripsi.csv'
data = load_data(data_path)

# Mengganti nilai cluster 0 menjadi 'tidak loyal' dan 1 menjadi 'loyal'
data['Cluster'] = data['Cluster'].replace({0: 'Tidak Loyal', 1: 'Loyal'})

# Menampilkan 20 Data Pertama
st.write("Data (8 baris pertama):")
st.dataframe(data.head(8))

# Statistik RFM per Cluster
st.write("Recency merupakan terakhir pelanggan melakukan transaksi")
st.write("Frequency menunjukkan berapa kali pelanggan melakukan transaksi")
st.write("Monetary merupakan jumlah uang yg dikeluarkan pelanggan selama melakukan transaksi")

# Filter data untuk setiap cluster
cluster_tidak_loyal = data[data['Cluster'] == 'Tidak Loyal']
cluster_loyal = data[data['Cluster'] == 'Loyal']

# Fungsi untuk mengambil statistik spesifik
def custom_describe(df):
    desc = df.describe(percentiles=[])
    return desc.loc[['count', 'mean', 'min', 'max']]

# Statistik untuk Cluster 'Tidak Loyal'
st.write("Cluster Tidak Loyal:")
st.write(custom_describe(cluster_tidak_loyal[['Recency', 'Frequency', 'Monetary']]))

# Statistik untuk Cluster 'Loyal'
st.write("Cluster Loyal:")
st.write(custom_describe(cluster_loyal[['Recency', 'Frequency', 'Monetary']]))

# Menampilkan Jumlah Pelanggan per Cluster
cluster_counts = data['Cluster'].value_counts()

# Menampilkan jumlah pelanggan dengan teks
st.write("Jumlah pelanggan di Cluster 'Tidak Loyal':", cluster_counts['Tidak Loyal'])
st.write("Jumlah pelanggan di Cluster 'Loyal':", cluster_counts['Loyal'])

# Menampilkan jumlah pelanggan dalam bentuk grafik batang
st.write("Visualisasi Jumlah Pelanggan per Cluster:")
fig, ax = plt.subplots()
ax.bar(cluster_counts.index, cluster_counts.values, color=['red', 'green'])
ax.set_xlabel('Cluster')
ax.set_ylabel('Jumlah Pelanggan')
ax.set_title('Jumlah Pelanggan per Cluster')
st.pyplot(fig)

