import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titel der App
st.title("Meine Streamlit App")

# Laden von Beispiel-Datensatz
@st.cache_data
def load_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"  # Beispiel-URL
    df = pd.read_csv(url)
    return df

data = load_data()

# Konvertiere Daten in numpy-Array
data_np = data.to_numpy()

# Anzeige der Daten
st.write("Daten:")
st.write(data.head())

# Beschreibung der Daten
st.write("Beschreibung der Daten:")
st.write(data.describe())

# Eingabefeld (Radio-Buttons) zur Steuerung der Anzeige
year = st.radio("Wähle ein Jahr", ['1958', '1959', '1960'])

# Mapping von Jahr zu Spaltenindex
year_column_map = {'1958': 1, '1959': 2, '1960': 3}

# Daten des ausgewählten Jahres extrahieren
selected_year_data = data_np[:, year_column_map[year]]

# Monate extrahieren
months = data_np[:, 0]

# Anzeige der Daten basierend auf der Auswahl
st.write(f"Angezeigtes Jahr: {year}")
fig, ax = plt.subplots()
ax.plot(months, selected_year_data, label=year)
ax.legend()
st.pyplot(fig)
