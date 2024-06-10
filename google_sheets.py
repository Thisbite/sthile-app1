import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Définir la portée
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Ajouter le chemin vers votre fichier credentials.json
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/credentials.json", scope)
client = gspread.authorize(creds)

# Ouvrir une feuille Google Sheets par son nom
sheet = client.open("Nom de votre feuille Google Sheets").sheet1

# Fonctions pour manipuler les données dans Google Sheets
def obtenir_donnees():
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

def ajouter_commande_tissus(date, type_tissu, quantite, cout):
    sheet.append_row([date, type_tissu, quantite, cout])

def ajouter_production(date, type_vetement, nombre, couleur, longueur_manche, taille, forme_cou, ouvrier):
    sheet.append_row([date, type_vetement, nombre, couleur, longueur_manche, taille, forme_cou, ouvrier])

def ajouter_performance_ouvrier(date, ouvrier, heure_arrivee, heure_depart, nombre_vetements, types_vetements):
    sheet.append_row([date, ouvrier, heure_arrivee, heure_depart, nombre_vetements, types_vetements])

def ajouter_vente(date, type_vetement, nombre, prix_vente, retouche, motif_retouche):
    sheet.append_row([date, type_vetement, nombre, prix_vente, retouche, motif_retouche])
