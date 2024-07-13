from produit import *
from vente import *
from sauvegarde import *


def menu_principal():
    print("1. Ajouter produits")
    print("2. Afficher produits")
    print("3. Rechercher produits")
    print("4. Enregistrer vente")
    print("5. Afficher ventes")
    print("6. Ventes par client")
    print("7. Générer le rapport de ventes")
    print("8. Chargement de données")
    print("9. Quitter")
    return input("Veuillez choisir une option: ")

def main():
    #charger_donnees()
    while True:
        choix = menu_principal()
        if choix == '1':
           ajouter_produit()
        elif choix == '2':
            afficher_produits()
        elif choix == '3':
            rechercher_produit()
        elif choix == '4':
           enregistrer_vente()
        elif choix == '5':
           afficher_ventes()
        elif choix == '6':
          ventes_par_client()
        elif choix == '7':
          generer_rapport_ventes()

        elif choix == '8':
            charger_donnees()

        elif choix == '9':
            print("        Merci, à la prochaine!         ")
            break
        else:
            print("         Désolé aucune option ne correspond à votre choix!         ")

if __name__ == "__main__":
    main()