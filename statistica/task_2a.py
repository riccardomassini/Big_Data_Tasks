import matplotlib.pyplot as plt
from itertools import product
import numpy as np

# Calcolo di tutte le possibili combinazioni e le relative somme
combinations = list(product(range(1, 7), repeat=2)) # Genera le possibili coppie
sums = [sum(pair) for pair in combinations] # Somme per ogni combinazione

# Calcolo della frequenza (quante volte una somma appare), valori unici (somme distinte) e della probabilità
unique_values, frequencies = np.unique(sums, return_counts=True)
probabilities = frequencies / sum(frequencies)

# Creazione del grafico step delle probabilità (grafico a gradini)
plt.step(unique_values, probabilities, where='mid', color='red', linewidth=2)
plt.title('Distribuzione della somma di due dadi (pdf)', fontsize=10)
plt.xlabel('Somma dei due dadi', fontsize=10)
plt.ylabel('Probabilità', fontsize=10)
plt.xticks(range(2, 13)) # Mostra i valori sull'asse delle x per le somme che ci servono
plt.grid(axis='y', linestyle='-', alpha=0.7)

# Mostra il grafico
plt.show()