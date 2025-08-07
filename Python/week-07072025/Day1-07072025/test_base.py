"""
#Niveau 1
print("===============Exercice 1 : Extraire des caractères individuels ou tranches simples======")

mot_1 = "Mardi"
for i in range(len(mot_1)):
    print(mot_1[i])

print("================ Exercice 2 : Inverser un mot ===================================")

mot_2 = " Samsung"
reverse = mot_2[::-1]
print(reverse)

print("============== Exercice 3 : Recuperer une sous chaine fixe===========================")

chaine = "Ceci est une chaine de caractère"
sous_chaine = chaine.split()
for i in range (len(sous_chaine)):
    print(sous_chaine[i])"""


#Niveau 2

print("============step & indexation négative======================")

#Afficher 1 caractère sur 2 à partir d’un certain indice

word = "Viveris"
print(word[0::2])

#Jouer avec -2, -1, ::-1, [::-2]

word_play = "Cristalline"
print(word_play[::3]) 

print("============Fonction à base slicing====================")

def isPalindrome(m:str):
    if (m[::-1]==m):
        print ("Is palindrome")
    else:
        print("Not palindrome")

m = input()
isPalindrome(m)