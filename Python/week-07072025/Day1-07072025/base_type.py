
a = 3
neg_num =-10
big_numb = 1_000_000 # Underscore the lisiblity

#print(a,big_numb,neg_num)

"""Focus on the operation"""

b : int = 10

print(b//a) # // --> La division entière, elle me retourne uniquement la partie entiere de la division

print(9//4) # <-- la division entiere

print ("=========================================================================================")
"""Les nombres flottant"""
c = 1.5e-4
print(c - b) # 1.5e-14 -->
""" Les nombres complexes"""

d = complex(2,5)

e = complex(7,4)
print(d + e)

print ("=========================================================================================")

print("Les chaines de caractère")

nom : str = "Samir"
print(nom)

chaine = "Perfectionne ses bases en programmation python. That's how i'm killing my time"

print(chaine)
print(nom + " "+ "est entrain de " + chaine)

print("==================Partie indexation dans les chaines de caractere===================================")

mot = "Informatique"
print(mot[0])

# Je peux faire un slicing sur le mot 
#Je vais afficher les 3 premieres lettres 
print(mot[0:3])

print(nom + " "+ "est fort en" + " "+ mot)
print("tous ce qui est" + " " + mot[:3] + " à 0 est négatif")


print(mot[0::2])

print("==================TEST METHODE ===================================")

mot = "Teranosaure est un dinosaure"
print(mot.split())

L = []
L = mot.split()
print(L)
print(L[0])
print(L[1:])