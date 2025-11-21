import warnings
warnings.filterwarnings("ignore", message="The frame.append method is deprecated")


from treatData import extract_data, filter_foncier_data, df_to_csv, read_csv
from agregateData import add_price_per_sqm, social_housing_rate, foncier_housing_median, aggregate_foncier_all


if __name__ == '__main__':

    ## local paths : to be changed when deploying
    rawData_absolute_path   = 'C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\raw\\'
    processed_data_path     = 'C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\processed\\'
    gold_data_path          = 'C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\gold\\'


    ############### SILVER -- CLEANING DATA : LOGEMENTS FONCIERS  ###############

    ## Raw data file path
    rawData                 = 'ValeursFoncieres-2020-S2.txt'
    source                  = rawData_absolute_path + rawData

    ## Process data file path
    processed_data_file      = 'LogementsFonciers_2020_S2.csv'
    processed_data_path      = processed_data_path + processed_data_file

    # data                    = extract_data(source)
    # filtered_data           = filter_foncier_data(data)

    # clean_df = add_price_per_sqm(filtered_data)
    # df_to_csv(clean_df, processed_data_path)

    ############### SILVER -- END OF CLEANING DATA  : LOGEMENT FONCIERS ###############



    ############### GOLD -- AGGREGATE : LOGEMENTS FONCIERS  ###############

    ## Agregate foncier housing rate per arrondissement
    all_silver_files = ["C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\processed\\LogementsFonciers_2020_S2.csv", 
                        "C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\processed\\LogementsFonciers_2021.csv",
                        "C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\processed\\LogementsFonciers_2022.csv",
                        "C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\processed\\LogementsFonciers_2023.csv",
                        "C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\processed\\LogementsFonciers_2024.csv",
                        "C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\processed\\LogementsFonciers_2025_S1.csv"]
    all_aggregate    = []

    for f in all_silver_files:
        # all_aggregate.append(foncier_housing_median(f))
        pass
    # concat_all = aggregate_foncier_all(all_aggregate)

    # df_to_csv(concat_all, gold_data_path+"AllFoncier_gold.csv")
    

    # test1 = foncier_housing_median(processed_data_path)
    # test2 = foncier_housing_median("C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\processed\\LogementsFonciers_2021.csv")
    # tt = aggregate_foncier_all([test1, test2])
    
    # print(tt.tail)

    ############### GOLD -- END OF AGGREGATE : LOGEMENTS FONCIERS  ###############



    ############### SILVER -- CLEANING AND AGGREGATING DATA  : LOGEMENTS SOCIAUX  ###############
    # Raw data file path
    rawData                 = 'logements-sociaux-finances-a-paris.csv'
    source                  = rawData_absolute_path + rawData

    # Process data file path
    processed_data_file      = 'Logements_Sociaux_gold.csv'
    processed_data_path      = gold_data_path + processed_data_file

    # data                     = read_csv(source)
    # filtered_data           = social_housing_rate(data)
    # df_to_csv(filtered_data, processed_data_path)

    ############### SILVER -- END OF CLEANING AND AGGREGATING DATA  : LOGEMENTS SOCIAUX ###############



    ############### CLEANING AND AGGREGATING DATA  : LOGEMENT 2 ###############





    ############### END OF CLEANING AND AGGREGATING DATA  : LOGEMENT 2 ###############
