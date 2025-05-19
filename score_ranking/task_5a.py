import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Ottieni il percorso assoluto alla cartella dello script principale
cartella_corrente = os.path.dirname(os.path.abspath(__file__))

# Costruisce il percorso assoluto alla cartella dello script con gli id
cartella_id = os.path.abspath(os.path.join(cartella_corrente, '..', 'config'))
sys.path.append(cartella_id)

from lista_id import id_5

# FUNZIONE PER CALCOLARE BMI (PESO/ALTEZZA^2)
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# RANGE DI CLASSIFICAZIONE DEL BMI
def bmi_range(bmi_value):
    if bmi_value < 18.5:
        return 'Sottopeso'
    if 18.5 <= bmi_value < 25:
        return 'Normapeso'
    if 25 <= bmi_value < 30:
        return 'Sovrappeso'
    else:
        return 'Obeso'

# COLORI DEI PUNTI SUL GRAFICO IN BASE ALLA CATEGORIA
colors = {'Sottopeso': 'yellow', 'Normapeso': 'green', 'Sovrappeso': 'red', 'Obeso': 'blue'}

public_url = f"https://docs.google.com/spreadsheets/d/{id_5}"
sheet_name_italians = "italiani"
sheet_name_athletes = "italiani_sportivi"

# LETTURA DATI DAL DATASET ITALIANI
italians_data = pd.read_excel(public_url + "/export?format=xlsx", sheet_name=sheet_name_italians)
height_italians = italians_data["Altezza (m)"].values
weight_italians = italians_data["Peso (kg)"].values

# LETTURA DATI DAL DATASET SPORTIVI
athletes_data = pd.read_excel(public_url + "/export?format=xlsx", sheet_name=sheet_name_athletes)
height_athletes = athletes_data["Altezza (m)"].values
weight_athletes = athletes_data["Peso (kg)"].values

# CALCOLO DEL BMI DELLE 2 CATEGORIE
bmi_italians = calculate_bmi(weight_italians, height_italians)
bmi_athletes = calculate_bmi(weight_athletes, height_athletes)

# RANGE DI CLASSI CLASSIFICHE DEL BMI PER LE 2 CATEGORIE
bmi_italians_classification = [bmi_range(bmi) for bmi in bmi_italians]
bmi_athletes_classification = [bmi_range(bmi) for bmi in bmi_athletes]

# CREAZIONE DEI 2 GRAFICI
_, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

for category, color in colors.items():
    italian_category = (np.array(bmi_italians_classification) == category) # Crea array booleani per la categoria italiani
    athlete_category = (np.array(bmi_athletes_classification) == category) # Crea array booleani per la categoria sportivi
    ax1.scatter(weight_italians[italian_category], height_italians[italian_category], color=color, label=category, s=8) # Grafico italiani con dimensione puntini uguale a 8
    ax2.scatter(weight_athletes[athlete_category], height_athletes[athlete_category], color=color, label=category, s=10) # Grafico sportivi con dimensione puntini uguale a 10

ax1.set_title("Distribuzione BMI degli Italiani")
ax1.set_xlabel("Peso (kg)")
ax1.set_ylabel("Altezza (m)")
ax1.legend()

ax2.set_title("Distribuzione BMI degli Sportivi")
ax2.set_xlabel("Peso (kg)")
ax2.set_ylabel("Altezza (m)")
ax2.legend()

# MOSTRA IL GRAFICO
plt.show()