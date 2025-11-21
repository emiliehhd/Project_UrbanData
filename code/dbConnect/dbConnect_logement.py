from pymongo import MongoClient
import pandas as pd


mongo_uri     = "mongodb+srv://Jeffflaj:Koukouda16@jeff.0lid4ok.mongodb.net/?retryWrites=true&w=majority"
client  = MongoClient(mongo_uri)
# db      = client["urban_data_silver"] #sliver db
db      = client["urban_data_gold"] #gold db


# collection = db["silver_logement"]
collection = db["logement"]


## Load the cleaned data
data_to_load = 'C:\\Users\\emili\\Desktop\\EFREI\\Projet_UrbanData\\data\\gold\\AllFoncier_gold.csv'
df = pd.read_csv(data_to_load, sep=",")  
# print(df.head())


# Prepare DataFrame for MongoDB insertion
df_mongo = pd.DataFrame({
    "annee": df["date"],
    "arrondissement": df["arrondissement"],
    "prix_median": df["median_price"],
    "surf_m2_median": df["median_surf_m2"],
    "nb_pieces_median": df["median_piece"],  
    "pourcent_logment": df["percent_house"],
    # "date_transaction": pd.to_datetime(df["Date"], errors='coerce'),
    "typologie": df["typology"],
    "variation_annuelle": df["annual_variation"]
})


## Insert data into MongoDB
# documents = df_mongo.to_dict(orient="records")
# collection.insert_many(documents)
# print(">>>Data inserted into MongoDB collection 'gold_logement'")

print(db.list_collection_names())

# print(collection.find_one())  # Display first document

