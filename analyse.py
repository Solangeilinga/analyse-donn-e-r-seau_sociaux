import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Task 2 – Generate random data for the social media data
# Nombre de posts à générer
n = 500

# Définir la liste des catégories
categories = ["Food", "Travel", "Fashion", "Fitness", "Music", "Culture", "Family", "Health"]

# Créer le dictionnaire avec des données aléatoires
data = {
    'Date': pd.date_range('2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}

# Créer un DataFrame pandas à partir du dictionnaire
df = pd.DataFrame(data)

# Task 3 – Load the data into a Pandas DataFrame and explore

# Le DataFrame est déjà créé dans Task 2 : df

# 1. Afficher les 5 premières lignes
print("Aperçu des 5 premières lignes :")
print(df.head())

# 2. Informations générales sur le DataFrame
print("\nInformations sur le DataFrame :")
print(df.info())

# 3. Statistiques descriptives pour les colonnes numériques
print("\nStatistiques descriptives :")
print(df.describe())

# 4. Compter le nombre de posts par catégorie
print("\nNombre de posts par catégorie :")
print(df['Category'].value_counts())

# Task 4 – Clean the data

# 1. Supprimer les valeurs nulles (NaN)
df = df.dropna()

# 2. Supprimer les doublons
df = df.drop_duplicates()

# 3. Convertir la colonne 'Date' en datetime
df['Date'] = pd.to_datetime(df['Date'])

# 4. Convertir la colonne 'Likes' en entier
df['Likes'] = df['Likes'].astype(int)

# Vérification après nettoyage
print("\nAprès nettoyage :")
print(df.info())
print(df.head())



# Task 5 – Visualize and Analyze the Data

# 1. Histogramme des Likes
plt.figure(figsize=(8,5))
sns.histplot(df['Likes'], bins=30, kde=True, color='skyblue')
plt.title("Distribution des Likes")
plt.xlabel("Likes")
plt.ylabel("Nombre de posts")
plt.show()

# 2. Boxplot Likes par catégorie
plt.figure(figsize=(10,6))
sns.boxplot(x='Category', y='Likes', data=df, palette='Set2')
plt.title("Likes par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Likes")
plt.xticks(rotation=45)
plt.show()

# 3. Statistiques générales
mean_likes = df['Likes'].mean()
print(f"\nMoyenne générale des Likes : {mean_likes:.2f}")

# 4. Moyenne des Likes par catégorie
mean_likes_by_category = df.groupby('Category')['Likes'].mean()
print("\nMoyenne des Likes par catégorie :")
print(mean_likes_by_category)
