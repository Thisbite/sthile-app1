import streamlit as st
import sqlite3
import pandas as pd
import data
from datetime import datetime


def page_commande():
    st.header("Enregistrement des Commandes de Tissus")

    with st.form("commande_tissus"):
        date_commande = st.date_input("Date de Commande")
        type_tissu = st.text_input("Type de Tissu")
        quantite = st.number_input("Quantité", min_value=0.0, step=0.1)
        cout = st.number_input("Coût", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            data.enregistrer_commande_tissus(date_commande, type_tissu, quantite, cout)
            st.success("Commande enregistrée avec succès.")

    return



def page_production():
    st.header("Suivi de la Production")

    with st.form("production_vetements"):
        date_production = st.date_input("Date de Production")
        serie_vet = st.text_input("Série de Vêtement")
        type_vetement = st.text_input("Type de Vêtement")
        nombre = st.number_input("Nombre Produit", min_value=0, step=1)
        couleur = st.text_input("Couleur")
        longueur_manche = st.selectbox("Longueur de Manche", ["Longue", "Courte", "Sans"])
        taille = st.selectbox("Taille", ["S", "M", "L", "XL", "XXL"])
        forme_cou = st.text_input("Forme du Col")
        ouvrier = st.text_input("Ouvrier Responsable")
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            date_production_str = date_production.strftime('%Y-%m-%d')  # Convertir la date en chaîne de caractères
            data.enregistrer_production(date_production_str, serie_vet, type_vetement, nombre, couleur, longueur_manche,
                                        taille, forme_cou, ouvrier)
            st.success("Production enregistrée avec succès.")

    return



def page_ventes():
    st.header("Suivi des Ventes")

    # Obtenir les types de vêtements disponibles
    types_vetements = data.obtenir_types_vetements()

    with st.form("ventes"):
        date_vente = st.date_input("Date de Vente")
        type_vetement = st.selectbox("Type de Vêtement", options=types_vetements)
        nombre = st.number_input("Nombre", min_value=0, step=1)
        prix_vente = st.number_input("Prix de Vente", min_value=0.0, step=0.01)


        retouche=st.checkbox("Retouche",key="retouche")
        motif_retouche = st.text_area("Motif de Retouche")
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            data.enregistrer_vente(date_vente, type_vetement, nombre, prix_vente, retouche, motif_retouche)
            st.success("Vente enregistrée avec succès.")
    return


def page_stock():
    st.header("État des Stocks")

    stock_data = data.obtenir_stock()
    st.write(stock_data)
    return




def page_acquisition():
    st.header("Enregistrement de l'Acquisition des Matières Premières")

    with st.form("acquisition_matiere"):
        date_acquisition = st.date_input("Date d'Acquisition")
        quantite_tissu = st.number_input("Quantité de Tissu (mètres)", min_value=0.0, step=0.1)
        matiere_tissu = st.text_input("Matière de Tissu")
        couleur_tissu = st.text_input("Couleur de Tissu")
        quantite_bobine_fil = st.number_input("Quantité de Bobine de Fil", min_value=0, step=1)
        quantite_bouton = st.number_input("Quantité de Bouton", min_value=0, step=1)
        quantite_bande_tissee = st.number_input("Quantité de Bande Tissée", min_value=0, step=1)
        collant_dur = st.number_input("Collant Dur (mètres)", min_value=0.0, step=0.1)
        collant_papier = st.number_input("Collant Papier (mètres)", min_value=0.0, step=0.1)
        viseline = st.number_input("Viseline (mètres)", min_value=0.0, step=0.1)
        popeline = st.number_input("Popeline (mètres)", min_value=0.0, step=0.1)
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            data.enregistrer_acquisition(date_acquisition, quantite_tissu, matiere_tissu, couleur_tissu,
                                         quantite_bobine_fil, quantite_bouton, quantite_bande_tissee, collant_dur,
                                         collant_papier, viseline, popeline)
            st.success("Acquisition enregistrée avec succès.")





def page_pointage():
    st.header("Enregistrement du Pointage des Ouvriers")

    with st.form("pointage_ouvrier"):
        date_pointage = st.date_input("Date de Pointage")
        ouvrier = st.text_input("Nom de l'Ouvrier")
        presence = st.selectbox("Présence", ["Présent", "Absent"])
        heure_arrivee = st.time_input("Heure d'Arrivée", datetime.now().time())
        heure_depart = st.time_input("Heure de Départ", datetime.now().time())
        motif = st.text_input("Motif (si absent)")

        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            date_pointage_str = date_pointage.strftime('%Y-%m-%d')  # Convertir la date en chaîne de caractères
            heure_arrivee_str = heure_arrivee.strftime(
                '%H:%M:%S')  # Convertir l'heure d'arrivée en chaîne de caractères
            heure_depart_str = heure_depart.strftime('%H:%M:%S')  # Convertir l'heure de départ en chaîne de caractères

            data.enregistrement_pointage(date_pointage_str, ouvrier, presence, heure_arrivee_str, heure_depart_str, motif)
            st.success("Pointage enregistré avec succès.")