import streamlit as st
import pandas as pd
from datetime import datetime
import data  # Assurez-vous que ce module contient les fonctions de manipulation des données
import plotly.express as px

# Page configuration
st.set_page_config(page_title="S'Thilé - Suivi et Évaluation", page_icon="👗", layout="wide")

# Title
st.title("S'Thilé - Suivi et Évaluation de la Production")


# Sidebar
st.sidebar.title("Menu")
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    page = st.sidebar.selectbox("Choisir une page", ["Connexion", "Enregistrement"])
else:
    page = st.sidebar.selectbox("Choisir une page",
                                ["Commandes de Tissus", "Production", "Performance des Ouvriers", "Ventes", "Stocks",  "Acquisition des Matières Premières","Rapports"])

# Enregistrement des utilisateurs
if page == "Enregistrement":
    st.header("Enregistrement des Utilisateurs")

    with st.form("enregistrement_utilisateur"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            if username and password:
                data.enregistrer_utilisateur(username, password)
                st.success("Utilisateur enregistré avec succès.")
            else:
                st.error("Veuillez remplir tous les champs.")

# Connexion des utilisateurs
elif page == "Connexion":
    st.header("Connexion des Utilisateurs")

    with st.form("connexion_utilisateur"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        submitted = st.form_submit_button("Se connecter")

        if submitted:
            user = data.verifier_utilisateur(username, password)
            if user:
                st.session_state['logged_in'] = True
                st.success("Connexion réussie.")
                st.experimental_rerun()
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect.")

# Commandes de Tissus
elif page == "Commandes de Tissus" and st.session_state['logged_in']:
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

# Production
elif page == "Production" and st.session_state['logged_in']:
    st.header("Suivi de la Production")

    with st.form("production"):
        date_production = st.date_input("Date de Production")
        type_vetement = st.text_input("Type de Vêtement")
        nombre = st.number_input("Nombre", min_value=1, step=1)
        couleur = st.text_input("Couleur")
        longueur_manche = st.text_input("Longueur de Manche")
        taille = st.text_input("Taille")
        forme_cou = st.text_input("Forme du Cou")
        ouvrier = st.text_input("Ouvrier")
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            data.enregistrer_production(date_production, type_vetement, nombre, couleur, longueur_manche, taille, forme_cou, ouvrier)
            st.success("Production enregistrée avec succès.")

# Performance des Ouvriers
elif page == "Performance des Ouvriers" and st.session_state['logged_in']:
    st.header("Évaluation de la Performance des Ouvriers")

    with st.form("performance_ouvriers"):
        date = st.date_input("Date")
        ouvrier = st.text_input("Ouvrier")
        heure_arrivee = st.time_input("Heure d'Arrivée")
        heure_depart = st.time_input("Heure de Départ")
        nombre_vetements = st.number_input("Nombre de Vêtements Confectionnés", min_value=0, step=1)
        types_vetements = st.text_area("Types de Vêtements Confectionnés")
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            data.enregistrer_performance_ouvrier(date, ouvrier, heure_arrivee, heure_depart, nombre_vetements, types_vetements)
            st.success("Performance enregistrée avec succès.")

# Ventes
elif page == "Ventes" and st.session_state['logged_in']:
    st.header("Suivi des Ventes")

    # Obtenir les types de vêtements disponibles
    types_vetements = data.obtenir_types_vetements()

    with st.form("ventes"):
        date_vente = st.date_input("Date de Vente")
        type_vetement = st.selectbox("Type de Vêtement", options=types_vetements)
        nombre = st.number_input("Nombre", min_value=1, step=1)
        prix_vente = st.number_input("Prix de Vente", min_value=0.0, step=0.01)
        retouche = st.checkbox("Retouche")
        motif_retouche = st.text_area("Motif de Retouche") if retouche else ""
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            data.enregistrer_vente(date_vente, type_vetement, nombre, prix_vente, retouche, motif_retouche)
            st.success("Vente enregistrée avec succès.")

# Stocks
elif page == "Stocks" and st.session_state['logged_in']:
    st.header("État des Stocks")

    stock_data = data.obtenir_stock()
    st.write(stock_data)



# Acquisition
elif page == "Acquisition des Matières Premières" and st.session_state['logged_in']:
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
            data.enregistrer_acquisition(date_acquisition, quantite_tissu, matiere_tissu, couleur_tissu, quantite_bobine_fil, quantite_bouton, quantite_bande_tissee, collant_dur, collant_papier, viseline, popeline)
            st.success("Acquisition enregistrée avec succès.")


# Rapports
elif page == "Rapports" and st.session_state['logged_in']:
    st.header("Rapports Statistiques")
    ventes_data = data.obtenir_ventes()
    if not ventes_data.empty:
        # Créer le diagramme circulaire
        st.subheader("Diagramme Circulaire des Types de Vêtements Vendus")
        fig = px.pie(ventes_data, names='Type de Vêtement', title='Répartition des Vêtements Vendus par Type')
        st.plotly_chart(fig)
    else:
        st.info("Aucune donnée de vente disponible .")
    st.header("Données statistiques")
    st.subheader("Tableaux de Ventes")

    st.write(ventes_data)

    st.subheader("Tableaux d'acquisition de matière première")
    matiere_data=data.obtenir_acquisitions()
    st.write(matiere_data)

    st.subheader("Tableaux de Production")
    production_data = data.obtenir_production()
    st.write(production_data)

    st.subheader("Tableaux des Performances des Ouvriers")
    performance_data = data.obtenir_performances()
    st.write(performance_data)



    # Vérifier s'il y a des données de ventes

