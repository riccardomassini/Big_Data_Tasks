import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Creazione array di valori e calcolo del valore assoluto di ciascun elemento
x = np.arange(-4, 5)
y = np.abs(x)

# Creazione tabella (valore originale - valore assoluto)
df = pd.DataFrame({"Valore originale": x, "Valore assoluto": y})

# Creazione del grafico a punti (scatter plot) con etichette e titolo
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='r', label="y = |x|", marker='o')
plt.xlabel("Valore originale (x)")
plt.ylabel("Valore assoluto (|x|)")
plt.title("Grafico a punti della funzione valore assoluto")
plt.axhline(0, color='gray', linewidth=0.5)  # Linea orizzontale su y=0
plt.axvline(0, color='gray', linewidth=0.5)  # Linea verticale su x=0
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Mostra il grafico
plt.show()

# Calcolo e stampa della correlazione di Pearson
pearson = df.corr().iloc[0, 1]
print(f"\nCoefficiente di correlazione di Pearson: {pearson:.30f}")