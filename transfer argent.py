

solde = 30000            # Solde initial
code_secret = "1234"     # Code PIN
tentatives_max = 3       # Tentatives de code


# Vérification du code PIN

def verifier_code():
    """Vérifie le code PIN avec 3 tentatives."""
    for tentative in range(1, tentatives_max + 1):
        saisie = input(" Entrez votre code secret : ")
        if saisie == code_secret:
            return True
        else:
            print(" Code incorrect.")
    print(" Trop de tentatives ! Compte bloqué temporairement.")
    return False


# Vérification numéro Togo

def numero_valide(numero):
    """Vérifie si le numéro est un numéro togolais valide."""
    prefixes = ("70", "71", "72", "73", "74", "75", "76", "77", "78", "79",
                "90", "91", "92", "93", "94", "95", "96", "97", "98", "99")
    return len(numero) == 8 and numero.isdigit() and numero.startswith(prefixes)



# Fonction de transfert

def transfert():
    global solde

    print("\n TRANSFERT D'ARGENT")
    numero = input("Numéro du bénéficiaire : ")

    if not numero_valide(numero):
        print(" Numéro invalide !")
        return

    montant = int(input("Montant à transférer : "))

    if montant <= 0:
        print(" Montant invalide.")
        return

    if montant > solde:
        print(" Solde insuffisant !")
        return

    print("\nCONFIRMATION DU TRANSFERT")
    print(f"  Montant : {montant} FCFA")
    print(f"  Bénéficiaire : {numero}\n")

    # Vérification du PIN
    if not verifier_code():
        return

    # Débit du solde
    solde -= montant

    print("\n Transfert effectué avec succès !")
    print(f" Nouveau solde : {solde} FCFA\n")



# Menu principal USSD

def afficher_menu():
    print("""

      QUELLE OPPERATION VOULEZ-VOUS EFFECTUER ?

1️  Vérifier mon solde
2️  Faire un transfert
0️  Quitter


""")



# PROGRAMME PRINCIPAL

while True:
    afficher_menu()
    choix = input("  Faites un choix : ")

    if choix == "1":
        print(f"\n Votre solde est : {solde} FCFA\n")

    elif choix == "2":
        transfert()

    elif choix == "0":
        print("\n Merci d'avoir utilisé notre service mobile money.")
        break

    else:
        print(" Choix invalide.\n")
