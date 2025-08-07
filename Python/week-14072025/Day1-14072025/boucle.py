words = "Mardi"
voy = ["a","i"]
for characters in words:
    if characters in voy:
        print(characters.strip())
    else :
        print("­")

for number in range(1,11):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    else:
        print("evennnnnn")

week = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
for index, day in enumerate(week):
    print(f"the day {day} est le jour {index+1} de la semaine")

count = 10
while count > 0:
    print(count)
    count -= 1


