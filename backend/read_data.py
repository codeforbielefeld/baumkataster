import pandas as pd
import pyproj
import sys

sys.path.insert(0, "..")
# settings.configure()
from ..baumkataster.models import Tree

# read data
df = pd.read_csv("./Jupyter/Data/einzelbaeume.csv", delimiter=";")

# rename columns
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

# convert Geoinformation in coordinates
projection = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')


def unproject(wkt):
    (x, y) = wkt.replace("POINT (", "").replace(")", "").split(" ")
    return projection(x, y, inverse=True)


df['coords'] = df["Geo"].apply(unproject)

print(df.head())

print(df[10])

for tree in df:
    tree = Tree(oid=tree.oid,
                name=tree.Baumart_Deutsch,
                height=tree.Baumhoehe,
                diameter=tree.Kronendurchmesser,
                lat=tree.coords[0],
                long=tree.coords[1],
                type_of_care=tree.Pflege_Art_Nummer,
                care_kind=tree.Plege_Art_Beschreibung,
                user_list=[]
                )
