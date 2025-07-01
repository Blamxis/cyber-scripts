# port_scanner.py

import socket  # C'est la bibliothèque qui permet de faire des connexions réseau (TCP/IP)

# On demande à l'utilisateur sur quelle machine (IP) il veut faire un scan
ip = input("Entrez l'adresse IP à scanner : ")

# Voici la liste des ports qu'on veut tester. Ce sont les plus classiques (FTP, SSH, HTTP, HTTPS...)
ports = [21, 22, 23, 80, 443, 8080]

print(f"\nScan de {ip} en cours...\n")

# On va tester chaque port un par un
for port in ports:
    # On crée un "socket", c'est un peu comme un téléphone qui essaie d'appeler un numéro (ici un port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPv4, SOCK_STREAM = TCP
    
    sock.settimeout(1)  # Si le port ne répond pas dans 1 seconde, on arrête d'attendre

    # On essaie de se connecter au port. Si le port répond, result = 0
    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"[+] Le port {port} est OUVERT ✅")
    else:
        print(f"[-] Le port {port} est fermé ❌")
    
    sock.close()  # On ferme le socket (on raccroche le téléphone)
print("\nScan terminé !")  # On affiche un message de fin