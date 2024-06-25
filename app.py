import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import data  # Assurez-vous que ce module contient les fonctions de manipulation des données
import plotly_express as px
import fonction_page as fp
conn = sqlite3.connect('sthile.db')
def load_data(table_name):
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, conn)






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
                                ["Ressources humaines","Ma boutique","Statistique boutique"])

# Enregistrement des utilisateurs
if page == "Utilisateur App":
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


elif page=="Ma boutique":
    fp.page_ventes()
    fp.page_production()
    fp.page_acquisition()
    fp.page_commande()
    fp.page_stock()




elif page=="Ressources humaines":
    fp.page_pointage()
    fp.page_employes()








# Rapports
elif page == "Statistique boutique" and st.session_state['logged_in']:
    st.header("Rapports Statistiques")
    # Charger les tables
    commandes = load_data('commandes')
    production = load_data('production')

    ventes = load_data('ventes')
    acquisitions = load_data('acquisitions')

    # Afficher les statistiques des ventes
    st.title("Statistiques des Ventes")

    # Total des ventes par mois
    ventes['date'] = pd.to_datetime(ventes['date'])
    ventes['mois'] = ventes['date'].dt.to_period('M')
    ventes_mensuelles = ventes.groupby('mois').agg({'nombre': 'sum', 'prix_vente': 'sum'}).reset_index()

    fig1 = px.bar(ventes_mensuelles, x='mois', y='nombre', title='Total des Ventes par Mois')
    st.plotly_chart(fig1)

    fig2 = px.bar(ventes_mensuelles, x='mois', y='prix_vente', title='Revenu des Ventes par Mois')
    st.plotly_chart(fig2)

    # Répartition des ventes par type de vêtement
    ventes_par_type = ventes.groupby('type_vetement').agg({'nombre': 'sum'}).reset_index()
    fig3 = px.pie(ventes_par_type, values='nombre', names='type_vetement',
                  title='Répartition des Ventes par Type de Vêtement')
    st.plotly_chart(fig3)

    # Afficher les statistiques de production
    st.title("Statistiques de Production")

    # Production par ouvrier
    production_par_ouvrier = production.groupby('ouvrier').agg({'nombre': 'sum'}).reset_index()
    fig4 = px.bar(production_par_ouvrier, x='ouvrier', y='nombre', title='Production par Ouvrier')
    st.plotly_chart(fig4)

    # Répartition des vêtements produits par type
    production_par_type = production.groupby('type_vetement').agg({'nombre': 'sum'}).reset_index()
    fig5 = px.pie(production_par_type, values='nombre', names='type_vetement',
                  title='Répartition des Vêtements Produits par Type')
    st.plotly_chart(fig5)


    st.title("Statistiques des Acquisitions")

    # Quantité de matières premières acquises
    acquisitions['date'] = pd.to_datetime(acquisitions['date'])
    acquisitions['mois'] = acquisitions['date'].dt.to_period('M')

    # Filtrer les colonnes numériques uniquement
    numerical_columns = ['quantite_tissu', 'quantite_bobine_fil', 'quantite_bouton', 'quantite_bande_tissee',
                         'collant_dur', 'collant_papier', 'viseline', 'popeline']
    acquisitions_mensuelles = acquisitions.groupby('mois')[numerical_columns].sum().reset_index()

    fig8 = px.bar(acquisitions_mensuelles, x='mois', y='quantite_tissu', title='Quantité de Tissu Acquis par Mois')
    st.plotly_chart(fig8)

    fig9 = px.bar(acquisitions_mensuelles, x='mois', y='quantite_bobine_fil',
                  title='Quantité de Bobines de Fil Acquises par Mois')
    st.plotly_chart(fig9)

    # Fermer la connexion à la base de données
    conn.close()


