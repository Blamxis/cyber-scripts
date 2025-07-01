# http_headers.py
import requests  # Bibliothèque pour faire des requêtes HTTP

# On demande à l'utilisateur l'URL à analyser
url = input("Entrez l'URL à scanner (avec https:// ou http://) : ")

try:
    # On envoie une requête HTTP GET à l'URL
    response = requests.get(url)

    # On récupère les en-têtes (headers) de la réponse
    headers = response.headers

    print(f"\n🧠 En-têtes HTTP pour {url} :\n")

    for key, value in headers.items():
        print(f"{key}: {value}")

except requests.exceptions.RequestException as e:
    print(f"❌ Erreur : impossible de se connecter à {url}")
    print(e)
