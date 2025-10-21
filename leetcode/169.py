# Liste d'exemple
nums = [1, 1, 3, 1, 1, 2, 5, 4, 2]

# -----------------------------
# Phase 1 : Trouver un candidat
# -----------------------------
candidate = None
count = 0

print("Étape | Nombre | Candidat | Compteur")
print("--------------------------------------")

for i, num in enumerate(nums):
    if count == 0:
        candidate = num  # nouveau candidat
    if num == candidate:
        count += 1
    else:
        count -= 1
    print(f"{i+1:5} | {num:7} | {candidate:9} | {count:8}")

# -----------------------------
# Phase 2 : Vérifier le candidat
# -----------------------------
if nums.count(candidate) > len(nums) // 2:
    print(f"\nÉlément majoritaire trouvé : {candidate}")
else:
    print(f"\nAucun élément majoritaire (dernier candidat : {candidate})")
