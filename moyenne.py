
etudiant = []
nb_etudiant = 5
nb_matiere = 5
for i in range(nb_etudiant):
    print("etudiant :", i+1)
    nom_etudiant = input("enter votre nom : ")
    somme = 0
    for j in range(nb_matiere):
        note = float(input("enter votre note : "))
        somme += note
        print(f"la note de chaque matiere {j+1} est : {note}")
    moyenne = somme / nb_matiere
    print(f"votre moyenne est : {moyenne}")
    etudiant.append([nom_etudiant, moyenne])
    