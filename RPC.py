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

# Créer un gestionnaire de requêtes XML-RPC personnalisé
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Créer un serveur XML-RPC
server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()

def get_siren_data(siren):
    """
    Retourne les données EgaPro pour un numéro SIREN donné.
    Un message d'erreur est retourné si le SIREN n'est pas trouvé.

    :param siren: Numéro SIREN en tant que chaîne de caractères
    :return: Les données correspondantes ou un message d'erreur
    """
    data = egapro_data.get(siren)
    if data is None:
        return {"erreur": "SIREN non trouvé"}
    return data

server.register_function(get_siren_data, 'get_siren_data')

# Exécuter le serveur XML-RPC
print("Le serveur RPC est en cours d'exécution sur http://localhost:8000/RPC2")
server.serve_forever()
