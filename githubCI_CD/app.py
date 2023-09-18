import pandas as pd

from sklearn.model_selection import train_test_split

import zipfile
import os


def load_data():
    return pd.read_csv('data/COURSE_house (1).csv')

def clean_data(data):
    # Supprimer les lignes dupliquées
    data = data.drop_duplicates()
    # Gérer les valeurs manquantes en les remplaçant
    for column in data.columns:
        data[column].fillna(data[column].mean, inplace=True)
    return data

def add_data(data):
    return data


def modify_data(data):
    return data

def divide_data(data):
    # Division des données

    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    return train_data, test_data

def save(train, test):

    df = pd.DataFrame(train)
    df.to_csv('train.csv', index=False)

    dff = pd.DataFrame(test)
    dff.to_csv('test.csv', index=False)

#if __name__=="__main__":
# Charger vos données

data = load_data()

# Appeler les fonctions en série
data = clean_data(data)

data = add_data(data)
data = modify_data(data)

train_data, test_data = divide_data(data)








