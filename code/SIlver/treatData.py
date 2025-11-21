#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import unicodedata

"""
extract_data: Extract data from source file
read_csv: Read CSV file into DataFrame
df_to_csv: Write DataFrame to CSV
remove_accents: Remove accents from text
filter_foncier_data: Filter the foncier data
"""


def extract_data(source: str):
    """Extract data from source"""
    with open(source, 'r') as file:
        data = file.read()
    return data


def read_csv(file_path: str) -> pd.DataFrame:
    """Read CSV file into DataFrame"""

    df = pd.read_csv(file_path, sep=";")  
    print(f">> Data read from {file_path}")
    return df


def df_to_csv(data_df: pd.DataFrame, output_file: str):
    """Write DataFrame to CSV"""
    data_df.to_csv(output_file, sep=",", index=False)
    print(f"Data saved to {output_file}")


def remove_accents(texte: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texte)
        if unicodedata.category(c) != 'Mn'
    )


def filter_foncier_data(data: str) -> pd.DataFrame:
    """Filter the foncier data"""

    col_to_extract      = {'Date mutation' : 8, 'Valeur fonciere' : 10, 'Code postal' : 16,'Surface Carrez du 1er lot' : 25, 
                            'Surface Carrez du 2eme lot' : 27, 'Surface Carrez du 3eme lot' : 29, 'Surface Carrez du 4eme lot' : 31,
                            'Surface Carrez du 5eme lot' : 33, 'Nombre de lots' : 34, 'Type local' : 36, 'Surface reelle bati' : 38, 
                            'Nombre pieces principales' : 39, 'Surface terrain' : 42}
    data_lines          = data.splitlines() 
    header              = ['Date', 'Valeur fonciere', 'Arrondissement','Surface Carrez du 1er lot', 'Surface Carrez du 2eme lot', 'Surface Carrez du 3eme lot', 'Surface Carrez du 4eme lot', 'Surface Carrez du 5eme lot', 'Nombre de lots', 'Type local', 'Surface reelle bati ', 'Nombre pieces principales' ,'Surface terrain']
    data_output_df      = pd.DataFrame(columns=header)
    
    for line in data_lines[1:]:
        new_line_out  = {}
        line_split = line.split('|')

        ## Filter : Paris only
        if line_split[16][0:2] != '75' or int(line_split[16][-2:]) > 20 or int(line_split[16][-2:]) < 1 or line_split[36] != ('Appartement' or 'Maison'):
            continue
        
        ## Clean and replace empty values by 0
        for i in range(len(line_split)):
            if line_split[i] == '':
                line_split[i] = '0'
            line_split[i] = remove_accents(line_split[i])  
            line_split[i] = line_split[i].replace(' ', '')  # for int conversion
            line_split[i] = line_split[i].replace(',', '.') # for float conversion

        new_line_out = {'Date' : int(line_split[8][-4:]), 'Valeur fonciere' : float(line_split[10]), 'Arrondissement' : int(line_split[16][-2:]), 'Surface Carrez du 1er lot' : float(line_split[25]), 
                            'Surface Carrez du 2eme lot' : float(line_split[27]), 'Surface Carrez du 3eme lot' : float(line_split[29]), 'Surface Carrez du 4eme lot' : float(line_split[31]),
                            'Surface Carrez du 5eme lot' : float(line_split[33]), 'Nombre de lots' : int(line_split[34]), 'Type local' : line_split[36], 'Surface reelle bati' : int(line_split[38]), 
                            'Nombre pieces principales' : int(line_split[39]), 'Surface terrain' : int(line_split[42])}
        
        data_output_df.loc[len(data_output_df)] = new_line_out
    
    return data_output_df


def filter_social_housing(df: pd.DataFrame):
    """Filter the social housing data"""

    col_to_extract      = {'Année du financement - agrément' : 4, 'Nombre total de logements financés' : 6, 'Arrondissement' : 13, 'Nature de programme' : 14}
    # data_lines          = data.splitlines() 
    header              = ['date_financement', 'nb_logement_total', 'arrondissement', 'type_programme']
    data_output_df      = pd.DataFrame(columns=header)

    print(data[1])

    for index, row in df.iterrows():

        print(index, row["nom"], row["age"])
    

# source = 'C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\raw\\logements-sociaux-finances-a-paris.csv'
# data = read_csv(source)
# filter_social_housing(data)