import json
from produit import *
ventes = []

def charger_ventes():
    global ventes
    try:
        with open('ventes.json', 'r') as file:
            ventes = json.load(file)
    except FileNotFoundError:
        ventes = []

def sauvegarder_ventes():
    with open('ventes.json', 'w') as file:
        json.dump(ventes, file, indent=4)

def enregistrer_vente():
    while True:
        print("         LES INFORMATIONS SUR LA VENTE          ")
       
        client = input("Entrez le nom du client: ")
        if client.isalpha():
            break
        else:
            print("Désolé ces caracteres ne sont pas autorisés.")

    while True:
        choix_recherche = input("Veuillez choisir le mode de recherche, par nom ou par ID ? (nom/id): ").lower()
        if choix_recherche in ['nom', 'id']:
            break
        else:
            print("Choix invalide, veuillez entrer 'nom' ou 'id'.")

    produit_trouve = None
    if choix_recherche == 'nom':
        while True:
            nom_produit = input("Entrez le nom du produit: ")
            if nom_produit.isalpha():
                produit_trouve = next((produit for produit in produits if produit['nom'] == nom_produit), None)
                if produit_trouve:
                    break
                else:
                    print("Produit non trouvé!.")
            else:
                print("Le nom du produit ne doit contenir que des lettres.")
    else:  # choix_recherche == 'id'
        while True:
            try:
                id_produit = int(input("Entrez l'ID du produit: "))
                produit_trouve = next((produit for produit in produits if produit['id_produit'] == id_produit), None)
                if produit_trouve:
                    break
                else:
                    print("Produit non trouvé.")
            except ValueError:
                print("Veuillez entrer un ID valide.")

    while True:
        try:
            quantite = int(input("Entrez la quantité vendue: "))
            if quantite > 0:
                break
            else:
                print("La quantité doit être un entier positif.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            
    date = input("Entrez la date de la vente (AAAA-MM-JJ): ")

    if produit_trouve['quantite'] >= quantite:
        vente = {'client': client, 'produit': produit_trouve['nom'], 'quantite': quantite, 'date': date}
        ventes.append(vente)
        produit_trouve['quantite'] -= quantite
        sauvegarder_ventes()
        sauvegarder_produits()  # Sauvegarder les produits mis à jour
        print("Vente enregistrée avec succès!")
    else:
        print("Quantité insuffisante en stock.")

def afficher_ventes():
    print("         AFFICHAGE DE LA VENTE         ")
    if not ventes:
        print("Aucune vente enregistrée.")
    else:
        for vente in ventes:
            print(f"Client: {vente['client']}, Produit: {vente['produit']}, Quantité: {vente['quantite']}, Date: {vente['date']}")


def ventes_par_client():
    print("         VENTE DU CLIENT         ")
    while True:
        client = input("Entrez le nom du client: ")
        if client.isalpha():
            break
        else:
            print("Le nom du client ne doit contenir que des lettres.")

    ventes_client = [vente for vente in ventes if vente['client'] == client]
    if not ventes_client:
        print("Aucune vente trouvée pour ce client.")
    else:
        for index, vente in enumerate(ventes_client, start=1):
            print(f"{index}. Produit: {vente['produit']}, Quantité: {vente['quantite']}, Date: {vente['date']}")

        choix_suppression = input("Voulez-vous supprimer une de ces ventes ? (oui/non): ").lower()
        if choix_suppression == "oui":
            try:
                numero_vente = int(input("Entrez le numéro de la vente à supprimer: "))
                vente_a_supprimer = ventes_client[numero_vente - 1]
                supprimer_vente(vente_a_supprimer)
                print("Vente supprimée avec succès")
            except (IndexError, ValueError):
                print("Numéro de vente invalide.")

def supprimer_vente(vente_a_supprimer):
    global ventes
    ventes = [vente for vente in ventes if vente != vente_a_supprimer]
    sauvegarder_ventes()


def charger_donnees(fichier):
    global produits, ventes
    with open(fichier, 'r') as f:
        data = json.load(f)
        produits = data.get('produits', [])
        ventes = data.get('ventes', [])
    print("Données chargées avec succès...")

def generer_rapport_ventes():
    print("         VOICI LE  RAPPORT DE VENTES         ")
    if not ventes:
        print("Aucune vente enregistrée.")
    else:
        for vente in ventes:
            print(f"Client: {vente['client']}, Produit: {vente['produit']}, Quantité: {vente['quantite']}, Date: {vente['date']}")


# Charger les ventes au démarrage
charger_ventes()
