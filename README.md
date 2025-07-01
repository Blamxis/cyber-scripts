# 🔎 Mini Scanner de Ports (Projet Cybersécurité débutant)

Bienvenue ! Ce petit script Python scanne quelques ports sur une machine (via son IP) et te dit s’ils sont ouverts ou non.

---

## 📌 À quoi ça sert ?

Ce script peut t’aider à :
- Comprendre comment fonctionne un scanner de ports
- Détecter si certains services sont actifs sur une machine (comme un serveur web ou SSH)
- Apprendre les bases du réseau en Python

---

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


