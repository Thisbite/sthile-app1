import streamlit as st
import sqlite3
import pandas as pd
import data
from datetime import datetime



def page_commande():
    st.markdown("""
    <style>
        /* Global styles */
        body {
            background-color: #f5f5f5;
            color: #333;
            font-family: Arial, sans-serif;
        }

        /* Header style */
        .stApp header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        /* Form container style */
        .form-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        /* Form field style */
        .form-container .stTextInput, .form-container .stDateInput, .form-container .stNumberInput {
            margin-bottom: 20px;
        }

        /* Button style */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.header("Enregistrement des Commandes de Tissus")

    with st.form("commande_tissus", clear_on_submit=True):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

        date_commande = st.date_input("Date de Commande")
        type_tissu = st.text_input("Type de Tissu")
        quantite = st.number_input("Quantité", min_value=0.0, step=0.1)
        cout = st.number_input("Coût", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            date_commande_str = date_commande.strftime('%Y-%m-%d')  # Convertir la date en chaîne de caractères

            data.enregistrer_commande_tissus(date_commande_str, type_tissu, quantite, cout)
            st.success("Commande enregistrée avec succès.")

        st.markdown('</div>', unsafe_allow_html=True)

    return



def page_production():
    st.markdown("""
    <style>
        /* Global styles */
        body {
            background-color: #f5f5f5;
            color: #333;
            font-family: Arial, sans-serif;
        }

        /* Header style */
        .stApp header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        /* Form container style */
        .form-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        /* Form field style */
        .form-container .stTextInput, .form-container .stDateInput, .form-container .stNumberInput, .form-container .stSelectbox {
            margin-bottom: 20px;
        }

        /* Button style */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.header("Suivi de la Production")

    with st.form("production_vetements", clear_on_submit=True):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

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

        st.markdown('</div>', unsafe_allow_html=True)

    return





def page_ventes():
    st.markdown("""
    <style>
        /* Global styles */
        body {
            background-color: #e0f7fa;  /* Bleu ciel */
            color: #333;
            font-family: Arial, sans-serif;
        }

        /* Header style */
        .stApp header {
            background-color: #0288d1;  /* Bleu plus foncé pour le contraste */
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        /* Form container style */
        .form-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        /* Form field style */
        .form-container .stTextInput, .form-container .stDateInput, .form-container .stNumberInput, .form-container .stSelectbox, .form-container .stTextArea, .form-container .stCheckbox {
            margin-bottom: 20px;
        }

        /* Button style */
        .stButton button {
            background-color: #0288d1;  /* Même bleu foncé pour les boutons */
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }

        /* Success message style */
        .stAlert {
            background-color: #d1ecf1;
            color: #0c5460;
            border-color: #bee5eb;
        }
    </style>
    """, unsafe_allow_html=True)

    st.header("Suivi des Ventes")

    # Obtenir les types de vêtements disponibles
    types_vetements = data.obtenir_types_vetements()

    with st.form("ventes"):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

        date_vente = st.date_input("Date de Vente")
        type_vetement = st.selectbox("Type de Vêtement", options=types_vetements)
        nombre = st.number_input("Nombre", min_value=0, step=1)
        prix_vente = st.number_input("Prix de Vente", min_value=0.0, step=0.01)

        retouche = st.checkbox("Retouche", key="retouche")
        motif_retouche = st.text_area("Motif de Retouche")
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            data.enregistrer_vente(date_vente, type_vetement, nombre, prix_vente, retouche, motif_retouche)
            st.success("Vente enregistrée avec succès.")

        st.markdown('</div>', unsafe_allow_html=True)

    return


def page_stock():
    st.markdown("""
    <style>
        /* Global styles */
        body {
            background-color: #e3f2fd;  /* Bleu clair */
            color: #333;
            font-family: Arial, sans-serif;
        }

        /* Header style */
        .stApp header {
            background-color: #1976d2;  /* Bleu foncé */
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        /* Table container style */
        .table-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        /* Table style */
        .stDataFrame {
            margin-bottom: 20px;
        }

    </style>
    """, unsafe_allow_html=True)

    st.header("État des Stocks")

    stock_data = data.obtenir_stock()
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write(stock_data)
    st.markdown('</div>', unsafe_allow_html=True)
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
    st.markdown("""
    <style>
        /* Global styles */
        body {
            background-color: #f5f5f5;
            color: #333;
            font-family: Arial, sans-serif;
        }

        /* Header style */
        .stApp header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        /* Form container style */
        .form-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        /* Form field style */
        .form-container .stTextInput, .form-container .stDateInput, .form-container .stSelectbox, .form-container .stTimeInput {
            margin-bottom: 20px;
        }

        /* Button style */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.header("Pointage des Ouvriers")

    with st.form("pointage_ouvrier", clear_on_submit=True):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

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

            data.enregistrement_pointage(date_pointage_str, ouvrier, presence, heure_arrivee_str, heure_depart_str,
                                         motif)
            st.success("Pointage enregistré avec succès.")

        st.markdown('</div>', unsafe_allow_html=True)

    return


def page_employes():
    st.markdown("""
    <style>
        /* Global styles */
        body {
            background-color: #f5f5f5;
            color: #333;
            font-family: Arial, sans-serif;
        }

        /* Header style */
        .stApp header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        /* Form container style */
        .form-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        /* Form field style */
        .form-container .stTextInput, .form-container .stDateInput, .form-container .stSelectbox {
            margin-bottom: 20px;
        }

        /* Button style */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.header("Enregistrement des Employés")

    with st.form("enregistrement_employe", clear_on_submit=True):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

        nom_prenoms = st.text_input("Nom et Prénoms")
        date_naissance = st.date_input("Date de Naissance")
        contact_telephone1 = st.text_input("Contact Téléphone 1", value="")
        contact_telephone2 = st.text_input("Contact Téléphone 2", value="")
        adresse_mail = st.text_input("Adresse Mail")
        fonction = st.text_input("Fonction")
        niveau_education = st.selectbox("Niveau d'Éducation", ["Aucun", "Primaire", "Secondaire", "Supérieur"])
        stat_matrimo = st.selectbox("Statut Matrimonial", ["Célibataire", "Marié", "Divorcé", "Veuf"])
        type_contrat = st.selectbox("Type de Contrat", ["CDI", "CDD", "Intérim", "Stage", "Journalier"])
        date_entre = st.date_input("Date d'Entrée")
        ville_origne = st.text_input("Ville d'Origine")
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            date_naissance_str = date_naissance.strftime('%Y-%m-%d')  # Convertir la date en chaîne de caractères
            date_entre_str = date_entre.strftime('%Y-%m-%d')  # Convertir la date en chaîne de caractères

            data.enregistrement_employe(nom_prenoms, date_naissance_str, contact_telephone1, contact_telephone2,
                                        adresse_mail, fonction, niveau_education, stat_matrimo, type_contrat,
                                        date_entre_str,
                                        ville_origne)
            st.success("Employé enregistré avec succès.")

        st.markdown('</div>', unsafe_allow_html=True)

    return
