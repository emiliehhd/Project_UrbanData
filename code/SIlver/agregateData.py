#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from treatData import extract_data, df_to_csv


"""
add_price_per_sqm: Calculate price per square meter and add as new column
foncier_housing_price_rate: Calculate foncier housing price rate per Arrondissement
social_housing_rate: Calculate social housing financing rate per Arrondissement for each year
"""


def add_price_per_sqm(df: pd.DataFrame) -> pd.DataFrame:
    """Sum the square meters and calculate price per square meter. Add the result as a new column."""

    df['Total Surface Carrez'] = df[['Surface Carrez du 1er lot', 'Surface Carrez du 2eme lot',
                                     'Surface Carrez du 3eme lot', 'Surface Carrez du 4eme lot',
                                     'Surface Carrez du 5eme lot']].sum(axis=1)
    
    df = df[df['Total Surface Carrez'] > 0]  # Avoid division by zero
    df.loc[df['Total Surface Carrez'] > 0, 'Prix par m2'] = df['Valeur fonciere'] / df['Total Surface Carrez']

    # Calculate median price per sqm by Arrondissement
    # median_price_df = df.groupby('Arrondissement')['Prix par m2'].median().reset_index(name='Median Prix par m2')

    return df


def foncier_housing_median(file_path: str) -> pd.DataFrame:
    """Calculate the """
    df      = pd.read_csv(file_path, sep=",")
    date    = df['Date'][0]
    
    ## new dataframe 
    header  = ['date', 'arrondissement','median_price', 'median_surf_m2', 'median_piece', 'percent_house', 'typology']    
    new_df  = pd.DataFrame(columns=header)
    rows    = [] 

    for arr in df['Arrondissement'].unique():
        nb_house        = df[df["Arrondissement"] == arr].shape[0]
        median_price    = df[df["Arrondissement"] == arr]['Prix par m2'].median()
        median_m2       = df[df["Arrondissement"] == arr]['Total Surface Carrez'].median()
        median_piece    = df[df["Arrondissement"] == arr]['Nombre pieces principales'].median()
        percent_house   = 100 * nb_house / df.shape[0]
        typology        = df['Type local'].unique()

        rows.append([date, arr, median_price, median_m2, median_piece, percent_house, typology])

    return pd.DataFrame(rows, columns=header)


def aggregate_foncier_all(files: list[pd.DataFrame]) -> pd.DataFrame:
    """Concatenate all foncier data and calculate the annual variation. The input files have to be ordered by ascending year"""
    
    df_final = files[0].copy()
    # print(df_final.head)

    first_date = True # used to calculate the annual variation

    for df in files:
        # calculate annual variation
        if not first_date:
            df["annual_variation"] = None
            actual_date = df['date'][0] # actual year
            prev_date   = actual_date - 1   # previous year
            # print(df.head)

            for arr in df['arrondissement'].unique():
                # print(df_final.head)
                print("\n\n", arr)
                print("\nllalalala", df_final.loc[(df_final['arrondissement'] == arr) & (df_final['date'] == prev_date), 'median_price'])
                print(df.loc[df['arrondissement'] == arr, 'median_price'])
                actual_price    = df.loc[df['arrondissement'] == arr, 'median_price']
                prev_price      = df_final.loc[(df_final['arrondissement'] == arr) & (df_final['date'] == prev_date), 'median_price']
                print(">>>>",(actual_price - prev_price) / prev_price)
                df.loc[df['arrondissement'] == arr, "annual_variation"] = (actual_price - prev_price) / prev_price
                # print(df.head)
            df_final = pd.concat([df_final, df], ignore_index=True)

        if first_date:
            df_final["annual_variation"] = 0.0 # we don't have the values of the previous years to compute the annual variation
            first_date = False
            # print(df_final.head)

    return df_final
            


def social_housing_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate the social housing financement rate per Arrondissement for each year"""
    
    # Group by Année du financement - agrément and Arrondissement to get total housing and social housing counts
    Nb_logements = df.groupby(['Année du financement - agrément', 'Arrondissement'])['Nombre total de logements financés'].sum().reset_index(name='Nombre total de logements financés')

    # Calculate sum of social housing per year and arrondissement
    final_df = pd.DataFrame(columns=['Annee_financement', 'Arrondissement', 'Nb_logements_sociaux', 'percent_logement_sociaux_finances'])

    for year in df['Année du financement - agrément'].unique():
        for arrondissement in df['Arrondissement'].unique():

            logements_sociaux = df[
                (df['Année du financement - agrément'] == year) &
                (df['Arrondissement'] == arrondissement)
            ]['Nombre total de logements financés'].sum()

            logement_sociaux_total = df[
                (df['Année du financement - agrément'] == year)
            ]['Nombre total de logements financés'].sum()

            final_df.loc[len(final_df)] = [
                year,
                arrondissement,
                logements_sociaux,
                100 * logements_sociaux / logement_sociaux_total
            ]
            final_df["Annee_financement"] = final_df["Annee_financement"].astype(int)
            final_df["Arrondissement"] = final_df["Arrondissement"].astype(int)
            final_df["Nb_logements_sociaux"] = final_df["Nb_logements_sociaux"].astype(int)

    return final_df
            