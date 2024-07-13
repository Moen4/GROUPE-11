import json

produits = []

def validation_nom_article(nom_article):
    if any(char.isdigit() for char in nom_article):
        print("Erreur ! le nom de l'article ne peut pas contenir de chiffres.")
        return False
    return True

def validation_prix_article(prix_article):
    try:
        float(prix_article)
        return True
    except ValueError:
        print("Erreur ! prix de l'article doit être un nombre.")
        return False

def validation_qte_article(qte_article):
    if qte_article.isdigit():
        return True
    else:
        print("Erreur ! la quantité de l'article doit être un nombre entier.")
        return False

def ajouter_produit():
    print("         VEUILLEZ IDENTIFIER VOTRE ARTICLE AVANT DE L'AJOUTER         ")
    id_produit = len(produits) + 1
    while True:
        nom = input("Entrez le nom du produit: ")
        if validation_nom_article(nom):
            break

    # Vérifier si le produit existe déjà
    for produit in produits:
        if produit['nom'].lower() == nom.lower():
            print("Erreur ! Le produit existe déjà.")
            return

    while True:
        prix = input("Entrez le prix du produit: ")
        if validation_prix_article(prix):
            prix = float(prix)
            break

    while True:
        quantite = input("Entrez la quantité du produit: ")
        if validation_qte_article(quantite):
            quantite = int(quantite)
            break

    produit = {'id_produit': id_produit, 'nom': nom, 'prix': prix, 'quantite': quantite}
    produits.append(produit)

    sauvegarder_produits()

    print("         PRODUIT AJOUTE AVEC SUCCÈS!         ")

def afficher_produits():
    if not produits:
        print("         PRODUIT NON DISPONIBLE!         ")
    else:
        print("         LISTE DE PRODUITS         ")
        for produit in produits:
            print(f"id_produit : {produit['id_produit']}, Nom: {produit['nom']}, Prix: {produit['prix']}, Quantité: {produit['quantite']}")

def rechercher_produit():
    print("         VEUILLEZ IDENTIFIER LE PRODUIT A RECHERCHER          ")
    choix = input("Voulez-vous rechercher par nom ou par ID? (nom/id): ").lower()
    produit_trouve = None

    if choix == "nom":
        nom = input("Entrez le nom du produit à rechercher: ")
        for produit in produits:
            if produit['nom'].lower() == nom.lower():
                produit_trouve = produit
                break
    elif choix == "id":
        id_produit = input("Entrez l'ID du produit à rechercher: ")
        if id_produit.isdigit():
            id_produit = int(id_produit)
            for produit in produits:
                if produit['id_produit'] == id_produit:
                    produit_trouve = produit
                    break

    if produit_trouve:
        print(f"Voici le produit recherché : id_produit: {produit_trouve['id_produit']}, Nom: {produit_trouve['nom']}, Prix: {produit_trouve['prix']}, Quantité: {produit_trouve['quantite']}")
        choix_modification = input("Voulez-vous modifier ce produit ? (oui/non): ").lower()
        if choix_modification == "oui":
            modifier_produit(produit_trouve['id_produit'])
            print("         LE PRODUIT A ETE MODIFIÉ AVEC SUCCÈS         ")
        choix_suppression = input("Voulez-vous supprimer ce produit ? (oui/non): ").lower()
        if choix_suppression == "oui":
            supprimer_produit(produit_trouve['id_produit'])
            print("         LE PRODUIT A ETE SUPPRIMÉ AVEC SUCCÈS         ")
    else:
        print("         CE PRODUIT EST INTROUVABLE!         ")

def modifier_produit(id_produit):
    for produit in produits:
        if produit['id_produit'] == id_produit:
            while True:
                nom = input(f"Entrez le nouveau nom du produit (actuel: {produit['nom']}): ")
                if validation_nom_article(nom):
                    produit['nom'] = nom
                    break

            while True:
                prix = input(f"Entrez le nouveau prix du produit (actuel: {produit['prix']}): ")
                if validation_prix_article(prix):
                    produit['prix'] = float(prix)
                    break

            while True:
                quantite = input(f"Entrez la nouvelle quantité du produit (actuelle: {produit['quantite']}): ")
                if validation_qte_article(quantite):
                    produit['quantite'] = int(quantite)
                    break

            sauvegarder_produits()
            break

def supprimer_produit(id_produit):
    global produits
    produits = [produit for produit in produits if produit['id_produit'] != id_produit]
    sauvegarder_produits()

def charger_produits():
    global produits
    try:
        with open('produits.json', 'r') as f:
            produits = json.load(f)
    except FileNotFoundError:
        produits = []

def mettre_a_jour_stock(produit_nom, quantite_vendue):
    for produit in produits:
        if produit['nom'].lower() == produit_nom.lower():
            produit['quantite'] -= quantite_vendue
            break

def verifier_stock(produit_nom, quantite_vendue):
    for produit in produits:
        if produit['nom'].lower() == produit_nom.lower():
            return produit['quantite'] >= quantite_vendue
    return False

def sauvegarder_produits():
    with open('produits.json', 'w') as f:
        json.dump(produits, f)

# Charger les produits au démarrage
charger_produits()
