import csv
import pyproj
import os
from supabase import create_client, Client

url = "http://127.0.0.1:54321"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0"

username = "baumkataster"
password = "12345678"
supabase_client: Client = create_client(url, key)

user = supabase_client.auth.sign_up({ "email": username, "password": password })
user = supabase_client.auth.sign_in_with_password({ "email": username, "password": password })


#transforms WKT to GEO
projection = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')
def unproject(wkt):
    (x, y) = wkt.replace("POINT (", "").replace(")", "").split(" ")
    return projection(x, y, inverse=True)

with open('./Jupyter/Data/einzelbaeume.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        print(row['oid'], row['baumart_de'], row['baumart_bo'], row['kronendurc'], row['pfle_art_n'], row['pfle_art_b'], row['baumhoehe_'], row['standort_n_output'], row['kronendurc_output'])
        coordinates = unproject(row['WKT'])

        # WKT
        # oid √
        # baumart_de √
        # baumart_bo √
        # kronendurc √
        # pfle_art_n -
        # pfle_art_b - 
        # baumhoehe_ √
        # standort_n_output 
        # kronendurc_output

        lat = coordinates[1],
        long = coordinates[0],

        supabase_client.table('trees').insert([
            {
                'id': row['oid'],
                'standortnr': row['oid'],
                'artdtsch': row['baumart_de'],
                'artbot': row['baumart_bo'],
                'baumhoehe': row['baumhoehe_'],
                'kronedurch': row['kronendurc'],
                'lat': lat[0],
                'lng': long[0],
            }
        ]).execute()


        print('')