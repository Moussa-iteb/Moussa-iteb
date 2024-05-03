import pandas as pd
atm_atb_csv =  "C:/Users/ACER/Downloads/Stat/atm_atb.csv"

# Lecture du fichier CSV en spécifiant le séparateur virgule
atm_atb = pd.read_csv(atm_atb_csv, sep='|')
atm_atb.head(10)

atm_trs_csv = "C:/Users/ACER/Downloads/Stat/atm_trs.csv"
atm_trs= pd.read_csv(atm_trs_csv, sep='|')
atm_trs.head(10)

branch_atb_csv = "C:/Users/ACER/Downloads/Stat/branch_atb.csv"
branch_atb= pd.read_csv(branch_atb_csv, sep='|')
branch_atb.head(10)

chadechargement_csv =  "C:/Users/ACER/Downloads/Stat/chadechargement.csv"
chadechargement= pd.read_csv(chadechargement_csv, sep='|')
chadechargement.head(10)
# Afficher les premières lignes du DataFrame avant le prétraitement
print("Avant le prétraitement :")
print(atm_atb.head())
# Supprimer les lignes contenant des valeurs manquantes
atm_atb.dropna(inplace=True)
# Afficher le type de données de chaque colonne
print("\nTypes de données de chaque colonne :")
print(atm_atb.dtypes)
# Afficher les premières lignes du DataFrame après le prétraitement
print("\nAprès le prétraitement :")
atm_atb.head(50)



# Afficher les premières lignes du DataFrame avant le prétraitement
print("Avant le prétraitement :")
print(atm_trs.head())
# Supprimer les lignes contenant des valeurs manquantes
atm_trs.dropna(inplace=True)
# Afficher le type de données de chaque colonne
print("\nTypes de données de chaque colonne :")
print(atm_trs.dtypes)
# Afficher les premières lignes du DataFrame après le prétraitement
print("\nAprès le prétraitement :")
print(atm_trs.head(50))
atm_trs.head(50)




# Afficher les premières lignes du DataFrame avant le prétraitement
print("Avant le prétraitement :")
print(branch_atb.head())
# Supprimer les lignes contenant des valeurs manquantes
branch_atb.dropna(inplace=True)
# Afficher le type de données de chaque colonne
print("\nTypes de données de chaque colonne :")
print(branch_atb.dtypes)
# Afficher les premières lignes du DataFrame après le prétraitement
print("\nAprès le prétraitement :")
branch_atb.head(50)





# Afficher les premières lignes du DataFrame avant le prétraitement
print("Avant le prétraitement :")
print(chadechargement.head())
# Supprimer les lignes contenant des valeurs manquantes
chadechargement.dropna(inplace=True)
# Afficher le type de données de chaque colonne
print("\nTypes de données de chaque colonne :")
print(chadechargement.dtypes)
# Afficher les premières lignes du DataFrame après le prétraitement
print("\nAprès le prétraitement :")
chadechargement.head(50)


"""
Connects to a SQL database using pyodbc
"""

import pyodbc

SERVER = 'LAPTOP-R6KKLHDD\SQLEXPRESS'
DATABASE = 'hadhemi'

connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE}'


# Try connecting to the database
try:
     conn = pyodbc.connect(connectionString)
     print("Connection established successfully.")
     conn.close()

except pyodbc.Error as e:
    print("Error connecting to SQL Server database:", e)



from sqlalchemy import create_engine

# Créer une connexion à la base de données avec SQLAlchemy
engine = create_engine('mssql+pyodbc://@LAPTOP-R6KKLHDD\SQLEXPRESS/hadhemi?driver=ODBC+Driver+17+for+SQL+Server', connect_args={'UID': 'your_username', 'PWD': 'your_password'})

# Créer une table à partir du DataFrame atm_atb
atm_atb.to_sql('atm_atb', engine, if_exists='replace', index=False)

# Créer une table à partir du DataFrame atm_trs
atm_trs.to_sql('atm_trs', engine, if_exists='replace', index=False)

# Créer une table à partir du DataFrame branch_atb
branch_atb.to_sql('branch_atb', engine, if_exists='replace', index=False)

# Créer une table à partir du DataFrame chadechargement
chadechargement.to_sql('chadechargement', engine, if_exists='replace', index=False)

print("Tables créées avec succès dans la base de données.")






