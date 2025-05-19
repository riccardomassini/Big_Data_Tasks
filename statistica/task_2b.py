import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import sys
import os

# Ottieni il percorso assoluto alla cartella dello script principale
cartella_corrente = os.path.dirname(os.path.abspath(__file__))

# Costruisce il percorso assoluto alla cartella dello script con gli id
cartella_id = os.path.abspath(os.path.join(cartella_corrente, '..', 'config'))
sys.path.append(cartella_id)

from lista_id import id_2

# Definisce l'URL pubblico del file excel
public_url = f"https://docs.google.com/spreadsheets/d/{id_2}"

# Legge un file excel che viene scaricato tramite l'endpoint /export
df = pd.read_excel(public_url + "/export?format=xlsx")

# Estrae le colonne dal DataFrame e le converte in liste
producerA_data = df["Vita Batteria A"].to_list()
producerB_data = df["Vita Batteria B"].to_list()

# Calcolo di media e deviazione standard
mean_A = np.mean(producerA_data)
std_dev_A = np.std(producerA_data)
mean_B = np.mean(producerB_data)
std_dev_B = np.std(producerB_data)

# Calcolo delle funzioni di densità di probabilità
pdf_A = stats.norm.pdf(producerA_data, loc=mean_A, scale=std_dev_A)
pdf_B = stats.norm.pdf(producerB_data, loc=mean_B, scale=std_dev_B)

_, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4)) # Tupla per rappresentare i 2 grafici

# Creazione del grafico per il produttore A
ax1.plot(producerA_data, pdf_A, label="Distribuzione Normale Produttore A", color='blue')
ax1.set_title("Distribuzione Normale Produttore A")
ax1.set_xlabel("Valore")
ax1.set_ylabel("Densità di probabilità")
ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.set_xlim(0, 100)

# Creazione del grafico per il produttore B
ax2.plot(producerB_data, pdf_B, label="Distribuzione Normale Produttore B", color='red')
ax2.set_xlabel("Valore")
ax2.set_ylabel("Densità di probabilità")
ax2.set_title("Distribuzione Normale Produttore B")
ax2.legend()
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.set_xlim(0, 100)

# Mostra il grafico
plt.show()