items = ["Vase", "Statue", "Mask"]
for index, item in enumerate(items, start=1):
    print(f"Exhibit {index} : {item} - Ancien Greece")
'-------------------------------------------------------------------------------------------'
class WeatherData:
    def __init__(self, temp_c, humidity):
        self.temp_c = temp_c
        self.humidity = humidity
    def display(self):
        print(f"Temperature: {self.temp_c}°C, Humidity: {self.humidity}%")
today = WeatherData(22, 45)
today.temp_c = 25
today.display()



"""Un système de validation des données utilise une fonction pour vérifier si une valeur se situe
dans une plage acceptable. Quel sera le résultat de la fonction suivante lors du
traitement d'une lecture de 32 par le capteur ?"""

def validate_temperature(reading): 
    if 20 <= reading <= 40: 
        result = "Valid" 
    else: 
        result = "Invalid" 
    return result

"""Un programme d'analyse des données traite les enregistrements financiers à l'aide du code suivant :"""

try: 
    file = open('financial_data.csv', 'r') 
    data = file.read() 
    #result = process_data(data) 
    #print(f"Total: ${result}") 
except FileNotFoundError: 
    print("Error: Financial data file not found.") 
except ValueError: 
    print("Error: Data contains invalid values.") 
finally: 
    file.close()


