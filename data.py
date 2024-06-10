import sqlite3
import pandas as pd
import hashlib

# Connexion à la base de données SQLite
conn = sqlite3.connect('sthile.db')
cursor = conn.cursor()


# Création des tables si elles n'existent pas déjà
def creer_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS commandes (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        type_tissu TEXT,
                        quantite REAL,
                        cout REAL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS production (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        type_vetement TEXT,
                        nombre INTEGER,
                        couleur TEXT,
                        longueur_manche TEXT,
                        taille TEXT,
                        forme_cou TEXT,
                        ouvrier TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS performances (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        ouvrier TEXT,
                        heure_arrivee TEXT,
                        heure_depart TEXT,
                        nombre_vetements INTEGER,
                        types_vetements TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ventes (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        type_vetement TEXT,
                        nombre INTEGER,
                        prix_vente REAL,
                        retouche INTEGER,
                        motif_retouche TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS acquisitions (
                            id INTEGER PRIMARY KEY,
                            date TEXT,
                            quantite_tissu REAL,
                            matiere_tissu TEXT,
                            couleur_tissu TEXT,
                            quantite_bobine_fil INTEGER,
                            quantite_bouton INTEGER,
                            quantite_bande_tissee INTEGER,
                            collant_dur REAL,
                            collant_papier REAL,
                            viseline REAL,
                            popeline REAL
                          )''')

    conn.commit()


# Appel à la création des tables au démarrage
creer_tables()


# Fonctions pour enregistrer les données
def enregistrer_commande_tissus(date, type_tissu, quantite, cout):
    cursor.execute('''INSERT INTO commandes (date, type_tissu, quantite, cout)
                      VALUES (?, ?, ?, ?)''', (date, type_tissu, quantite, cout))
    conn.commit()


def enregistrer_production(date, type_vetement, nombre, couleur, longueur_manche, taille, forme_cou, ouvrier):
    cursor.execute('''INSERT INTO production (date, type_vetement, nombre, couleur, longueur_manche, taille, forme_cou, ouvrier)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (date, type_vetement, nombre, couleur, longueur_manche, taille, forme_cou, ouvrier))
    conn.commit()


def enregistrer_performance_ouvrier(date, ouvrier, heure_arrivee, heure_depart, nombre_vetements, types_vetements):
    heure_arrivee_str = heure_arrivee.strftime('%H:%M')
    heure_depart_str = heure_depart.strftime('%H:%M')
    cursor.execute('''INSERT INTO performances (date, ouvrier, heure_arrivee, heure_depart, nombre_vetements, types_vetements)
                      VALUES (?, ?, ?, ?, ?, ?)''', (date, ouvrier, heure_arrivee_str, heure_depart_str, nombre_vetements, types_vetements))
    conn.commit()


def enregistrer_vente(date, type_vetement, nombre, prix_vente, retouche, motif_retouche):
    cursor.execute('''INSERT INTO ventes (date, type_vetement, nombre, prix_vente, retouche, motif_retouche)
                      VALUES (?, ?, ?, ?, ?, ?)''', (date, type_vetement, nombre, prix_vente, retouche, motif_retouche))
    conn.commit()


def enregistrer_utilisateur(username, password):
    password_hashed = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('''INSERT INTO utilisateurs (username, password)
                      VALUES (?, ?)''', (username, password_hashed))
    conn.commit()


def verifier_utilisateur(username, password):
    password_hashed = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('''SELECT * FROM utilisateurs WHERE username=? AND password=?''', (username, password_hashed))
    user = cursor.fetchone()
    return user


# Fonctions pour obtenir les données
def obtenir_ventes():
    cursor.execute('SELECT * FROM ventes')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['ID', 'Date', 'Type de Vêtement', 'Nombre', 'Prix de Vente', 'Retouche',
                                     'Motif de Retouche'])
    return df


def obtenir_production():
    cursor.execute('SELECT * FROM production')
    data = cursor.fetchall()
    df = pd.DataFrame(data,
                      columns=['ID', 'Date', 'Type de Vêtement', 'Nombre', 'Couleur', 'Longueur de Manche', 'Taille',
                               'Forme du Cou', 'Ouvrier'])
    return df


def obtenir_performances():
    cursor.execute('SELECT * FROM performances')
    data = cursor.fetchall()
    df = pd.DataFrame(data,
                      columns=['ID', 'Date', 'Ouvrier', 'Heure d\'Arrivée', 'Heure de Départ', 'Nombre de Vêtements',
                               'Types de Vêtements'])
    return df


def obtenir_types_vetements():
    cursor.execute('SELECT DISTINCT type_vetement FROM production')
    data = cursor.fetchall()
    types_vetements = [row[0] for row in data]
    return types_vetements



def enregistrer_acquisition(date, quantite_tissu, matiere_tissu, couleur_tissu, quantite_bobine_fil, quantite_bouton, quantite_bande_tissee, collant_dur, collant_papier, viseline, popeline):
    cursor.execute('''INSERT INTO acquisitions (date, quantite_tissu, matiere_tissu, couleur_tissu, quantite_bobine_fil, quantite_bouton, quantite_bande_tissee, collant_dur, collant_papier, viseline, popeline)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (date, quantite_tissu, matiere_tissu, couleur_tissu, quantite_bobine_fil, quantite_bouton, quantite_bande_tissee, collant_dur, collant_papier, viseline, popeline))
    conn.commit()




# Acquisition de matiere
def obtenir_acquisitions():
    cursor.execute('SELECT * FROM acquisitions')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['ID', 'Date', 'Quantité de Tissu', 'Matière de Tissu', 'Couleur de Tissu', 'Quantité de Bobine de Fil', 'Quantité de Bouton', 'Quantité de Bande Tissée', 'Collant Dur', 'Collant Papier', 'Viseline', 'Popeline'])
    return df



def obtenir_stock():
    cursor.execute('''
        SELECT type_vetement, SUM(nombre) as nombre_produit
        FROM production
        GROUP BY type_vetement
    ''')
    production = cursor.fetchall()
    cursor.execute('''
        SELECT type_vetement, SUM(nombre) as nombre_vendu
        FROM ventes
        GROUP BY type_vetement
    ''')
    ventes = cursor.fetchall()

    stock = {}
    for row in production:
        stock[row[0]] = {'produit': row[1], 'vendu': 0}
    for row in ventes:
        if row[0] in stock:
            stock[row[0]]['vendu'] = row[1]

    stock_data = [{'Type de Vêtement': k, 'Stock Disponible': v['produit'] - v['vendu']} for k, v in stock.items()]
    df = pd.DataFrame(stock_data)
    return df
