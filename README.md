# 🔐 cyber-scripts – Projets Cybersécurité Débutant

Bienvenue dans ce petit repo de scripts Python orientés cybersécurité !  
Chaque script a pour but d’apprendre en développant des outils simples, concrets et utiles pour découvrir le monde de la sécurité informatique.

---

## 🧰 Scripts inclus dans ce projet

### 1. `port_scanner.py` – Scanner de ports TCP

Ce script teste une liste de ports (comme 22, 80, 443...) sur une adresse IP et indique ceux qui sont ouverts ou fermés.

📌 Objectif :
- Comprendre comment fonctionne un scanner de ports
- S’initier à `socket` en Python
- Identifier les services accessibles sur une machine

## ⚙️ Comment l’utiliser ?

1. Ouvre un terminal
2. Lance le script :

```bash
python port_scanner.py

```
---

### 2. `http_headers.py` – Analyseur d’en-têtes HTTP

Ce script envoie une requête HTTP vers une URL et affiche les **en-têtes HTTP** renvoyés par le serveur.

📌 Objectif :
- Voir les infos techniques d’un serveur web
- Détecter certains en-têtes de sécurité (comme `X-Frame-Options`, `Content-Type`, etc.)
- Pratiquer les requêtes HTTP avec `requests`

## ⚙️ Comment l’utiliser ?

1. Ouvre un terminal
2. Lance le script :

```bash
python http_headers.py

```
---

### 3. `ftp_bruteforce.py` – Bruteforce d'accès FTP (par dictionnaire)

Ce script tente de se connecter à un serveur FTP en testant une série de mots de passe à partir d’un fichier `.txt` (wordlist).

📌 Objectif :
- Comprendre le principe du bruteforce
- Manipuler la lib `ftplib` pour se connecter à un FTP
- Automatiser une attaque par dictionnaire

## ⚙️ Comment l’utiliser ?

1. Ouvre un terminal
2. Lance le script :

```bash
python ftp_bruteforce.py

```

---
## ⚠️ Avertissement légal 

⚠️ **Ce script est à but pédagogique uniquement.**

Tu ne dois scanner que des machines que tu possèdes ou pour lesquelles tu as une autorisation explicite.

- 📌 Un exemple de machine que tu peux utiliser légalement pour tester :
- 👉 scanme.nmap.org (fournie par les créateurs de Nmap, autorisée aux scans publics simples).

---

## 📚 Infos utiles pour débutants

### 🔍 Qu’est-ce qu’un port ?

Un port, c’est comme une **porte d’entrée virtuelle** sur une machine.  
Chaque service (ex : site web, SSH, FTP) "écoute" sur un port spécifique pour répondre aux connexions.

### 🔢 Liste des ports testés par défaut dans `port_scanner.py` :

| Port | Service         | Utilité                         |
|------|------------------|----------------------------------|
| 21   | FTP              | Transfert de fichiers            |
| 22   | SSH              | Connexion distante sécurisée     |
| 23   | Telnet           | Ancien accès distant             |
| 80   | HTTP             | Sites web classiques             |
| 443  | HTTPS            | Sites web sécurisés              |
| 8080 | HTTP alternatif  | Serveurs web locaux ou en dev    |

🔧 Tu peux modifier cette liste dans la ligne `ports = [...]` dans le script.

---

## 👤 Auteur

- **Nom :** Maxime 
- **GitHub :** [@Blamxis](https://github.com/Blamxis)

Ce projet fait partie de ma formation autodidacte en cybersécurité.  
Il s'agit de mes premiers outils réseau, pensés pour **apprendre en créant**.

---

## 🌟 Support

Si tu trouves ce projet utile ou que tu apprends quelque chose :

⭐ Laisse une étoile sur ce repo  
🍴 Forke-le et améliore-le à ta sauce  
💬 Ouvre une issue si tu veux discuter ou proposer une idée


