import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Ottieni il percorso assoluto alla cartella dello script principale
cartella_corrente = os.path.dirname(os.path.abspath(__file__))

# Costruisce il percorso assoluto alla cartella dello script con gli id
cartella_id = os.path.abspath(os.path.join(cartella_corrente, '..', 'config'))
sys.path.append(cartella_id)

from lista_id import id_3

# Definisce l'URL pubblico del file excel e il nome del foglio
public_url = f"https://docs.google.com/spreadsheets/d/{id_3}"
sheet_name = "traffico_milanese"

# Legge un file excel che viene scaricato tramite l'endpoint /export
df = pd.read_excel(public_url + "/export?format=xlsx", sheet_name=sheet_name)

# Fissa i valori della prima settimana
fixed_wk = df['Traffico'][:7]

# Calcola l'autocorrelazione tra la prima settimana e le successive con shift
autocorrelations = []
for shift in range(1, len(df['Traffico']) - 6):
  lag = df['Traffico'][shift:shift + 7]
  autocorrelation = np.corrcoef(fixed_wk, lag)[0, 1]
  autocorrelations.append(autocorrelation)

# Crea i grafici con evidenza sui punti riscontrati
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Grafico Traffico
ax1.plot(range(len(df['Traffico'])), df['Traffico'], marker='o', linestyle='-', color='r', markersize=5)
ax1.set_title('Traffico', fontsize=18)
ax1.set_xlabel('Giorni', fontsize=12)
ax1.set_ylabel('Traffico', fontsize=12)
ax1.set_xticks(range(len(df['Traffico'])))
ax1.grid(True)

# Grafico Autocorrelazione
ax2.plot(range(1, len(autocorrelations) + 1), autocorrelations, marker='o', linestyle='-', color='b', markersize=5)
ax2.set_title('Autocorrelazione', fontsize=18)
ax2.set_xlabel('Shift in Giorni', fontsize=12)
ax2.set_ylabel('Coeff. Autocorrelazione', fontsize=12)
ax2.set_xticks(range(1, len(autocorrelations) + 1))
ax2.grid(True)

plt.tight_layout()
plt.show()