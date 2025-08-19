import pandas as pd

csv_path = 'data/capteurs.csv'
df = pd.read_csv(csv_path)
print(df.head())
print(dir(df))

#x = df [['temperature_c','pressure_hpa']]
#print(x)

"""
data = [10,20,30,40,50]
s = pd.Series(data)
print(s)

#Dataframe à partir d'un dictionnaire
data = { 'Nom' : ['Yannick', 'Wendy', 'Maryse', 'Anna'],
         'Age': [26, 25, 21, 17] }
df = pd.DataFrame(data)
print(df)

#Acceder aux differentes colums
print(df['Nom'])
print(df['Age'])
"""

"""# Pour acceder aux lignes
print(df.iloc[2,1])"""