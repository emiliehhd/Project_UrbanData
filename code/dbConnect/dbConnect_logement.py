from pymongo import MongoClient
import pandas as pd





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


