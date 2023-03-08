from django.core.management.base import BaseCommand
import random
import pandas as pd
import csv
import pyproj

from baumkataster.models import Tree

#convert Geoinformation in coordinates
projection = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')
#transforms WKT to GEO
def unproject(wkt):
    (x, y) = wkt.replace("POINT (", "").replace(")", "").split(" ")
    return projection(x, y, inverse=True)

class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')

        #read data
        df = pd.read_csv("./Jupyter/Data/einzelbaeume.csv", delimiter=";")

        #rename columns
        df = df.rename(columns={
            "WKT": "Geo",
            "baumart_de": "Baumart_Deutsch",
            "baumart_bo": "Baumart_Botanisch",
            "kronendurc": "Kronendurchmesser",
            "pfle_art_n": "Pflege_Art_Nummer",
            "pfle_art_b": "Pflege_Art_Beschreibung",
            "baumhoehe_": "Baumhoehe",
            "standort_n_output": "FRAGEZEICHEN",
            "kronendurc_output": "Kronendurchmesser_gerundet"
        })

        df['coords'] = df["Geo"].apply(unproject)
        #print(df.head())
        
        for index, tree in df.iterrows():
   
            tree = Tree(oid = tree.oid,
                        name = tree.Baumart_Deutsch,
                        height = tree.Baumhoehe,
                        diameter = tree.Kronendurchmesser,
                        lat = tree.coords[1],
                        long = tree.coords[0],
                        type_of_care = tree.Pflege_Art_Nummer,
                        care_kind = tree.Pflege_Art_Beschreibung,
                        )
            tree.save()

        self.stdout.write('done.')