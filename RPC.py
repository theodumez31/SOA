from csv import DictReader
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

# Initialiser les données EgaPro
egapro_data = {}

with open("index-egalite-fh-utf8.csv", encoding='utf-8') as csv_file:
    reader = DictReader(csv_file, delimiter=";", quotechar='"')
    for row in reader:
        siren = row["SIREN"]
        # Stocker ou mettre à jour les données pour le SIREN donné
        if siren not in egapro_data or egapro_data[siren]["Année"] < row["Année"]:
            egapro_data[siren] = row