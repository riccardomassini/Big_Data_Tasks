import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
import pandas as pd
import numpy as np
import itertools
import kagglehub

# Download del dataset 'World Happiness Report 2019' da Kaggle
path = kagglehub.dataset_download("PromptCloudHQ/world-happiness-report-2019")
df = pd.read_csv(path + "/world-happiness-report-2019.csv") # Lettura csv
df = df.dropna() # Rimuove righe con valori NaN
df.columns = df.columns.str.replace('\n', ' ', regex=True)

# Stampa della matrice di correlazione ed estrazione dei valori dalle colonne
# Selezione di tutte le colonne numeriche per l'analisi
numeric_df = df.select_dtypes(include=np.number)
correlation_matrix = numeric_df.corr()

# Calcolo dei coefficienti di correlazione, di r² e della significatività statistica (con alpha = 0.05)
# Creazione di un dizionario delle sole colonne numeriche per facilitare l'iterazione
numeric_variables = {col: df[col] for col in numeric_df.columns}

alpha = 0.05

print("CORRELAZIONI TRA TUTTE LE COPPIE DI VARIABILI NUMERICHE:\n")

# Calcola tutte le combinazioni a coppie delle variabili numeriche
for (label_x, series_x), (label_y, series_y) in itertools.combinations(numeric_variables.items(), 2):
    r, p = pearsonr(series_x, series_y)
    r_squared = r**2

    print(f"{label_x} ↔ {label_y}")
    print(f" - Coeff. Pearson: {r:.4f}")
    print(f" - r²: {r_squared:.4f}")
    print(f" - p-value: {p:.4f}")
    if p < alpha:
        print(" - La correlazione è statisticamente significativa (p < 0.05)\n")
    else:
        print(" - La correlazione non è statisticamente significativa (p ≥ 0.05)\n")

# Trova le colonne con la correlazione (assoluta) più alta
# Esclusione della diagonale e dei duplicati
corr_matrix = correlation_matrix.abs()  # Considera il valore assoluto della correlazione
upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Trova la coppia con la correlazione massima
max_corr_value = upper_triangle.max().max()
max_corr_pair = upper_triangle.stack().idxmax()

# Matrice di confusione delle correlazioni
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="Blues", square=True, linewidths=0.5, linecolor='white')
plt.title("Matrice di Correlazione - World Happiness Report 2019")
plt.tight_layout()
plt.show()

print(f"\nCOPPIA DI VARIABILI CON LA CORRELAZIONE PIÙ ALTA (in valore assoluto):")
print(f"{max_corr_pair[0]} ↔ {max_corr_pair[1]}")
print(f" - Correlazione: {max_corr_value:.4f}")