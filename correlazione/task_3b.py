import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
import sys
import os

# Ottieni il percorso assoluto alla cartella dello script principale
cartella_corrente = os.path.dirname(os.path.abspath(__file__))

# Costruisce il percorso assoluto alla cartella dello script con gli id
cartella_id = os.path.abspath(os.path.join(cartella_corrente, '..', 'config'))
sys.path.append(cartella_id)

from lista_id import id_3

# Funzione per formattare i valori sull'asse delle y a 4 cifre decimali
def format_func(value, tick_number):
    return f'{value:.4f}'

# Definisce l'URL pubblico del file excel e il nome del foglio
public_url = f"https://docs.google.com/spreadsheets/d/{id_3}"
sheet_name = "tabella_mollier"

# Legge un file excel che viene scaricato tramite l'endpoint /export
df = pd.read_excel(public_url + "/export?format=xlsx", sheet_name=sheet_name)

# Estrazione dei valori di Temperatura e Volume da Excel
x = df["T (°C)"].values.reshape(-1, 1)
y = df["Vi (l)"].values

# Creazione del modello di regressione lineare
model = LinearRegression(fit_intercept=False)
model.fit(x, y) # Addestramento modello sui nostri dati
y_fit = model.predict(x) # Previsione valori

# Creazione del grafico a punti (scatter plot con outlier in rosso)
plt.figure(figsize=(8,5)) # Creazione grafico
outlier_index = df["Vi (l)"].idxmax() # Identificazione outlier (valore massimo di Vi (l))
plt.scatter(x=df["T (°C)"], y=df["Vi (l)"], color="yellow", edgecolor="black", s=100)
plt.scatter(df["T (°C)"].iloc[outlier_index], df["Vi (l)"].iloc[outlier_index], color="red", edgecolor="black", s=100)
plt.xlabel("Temperatura (°C)")
plt.ylabel("Volume (l)")
plt.title("Grafico Temperatura vs Volume")
plt.grid()
plt.xlim(0, 400)
plt.ylim(0, 0.25)
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_func)) # Mostra 4 cifre decimali sull'asse delle y
plt.plot(x, y_fit, color='black', linestyle='--') # Retta di regressione

# Mostra il grafico
plt.show()

# Calcolo dei coefficienti di correlazione e stampa
pearson_coef, _ = pearsonr(df['T (°C)'], df['Vi (l)'])
spearman_coef, _ = spearmanr(df['T (°C)'], df['Vi (l)'])
print(f"\nCoefficiente di Pearson: {pearson_coef:.4f}")
print(f"Coefficiente di Spearman: {spearman_coef:.4f}")