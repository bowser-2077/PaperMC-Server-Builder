import tkinter as tk
from tkinter import ttk, messagebox
import os
import subprocess
import requests
import threading

# Fonction pour obtenir les versions du serveur Minecraft
def get_versions():
    return {
"1.21.4": "https://api.papermc.io/v2/projects/paper/versions/1.21.4/builds/130/downloads/paper-1.21.4-130.jar",
    "1.21.3": "https://api.papermc.io/v2/projects/paper/versions/1.21.3/builds/82/downloads/paper-1.21.3-82.jar",
    "1.21.1": "https://api.papermc.io/v2/projects/paper/versions/1.21.1/builds/132/downloads/paper-1.21.1-132.jar",
    "1.21": "https://api.papermc.io/v2/projects/paper/versions/1.21/builds/130/downloads/paper-1.21-130.jar",
    "1.20.6": "https://api.papermc.io/v2/projects/paper/versions/1.20.6/builds/151/downloads/paper-1.20.6-151.jar",
    "1.20.5": "https://api.papermc.io/v2/projects/paper/versions/1.20.5/builds/22/downloads/paper-1.20.5-22.jar",
    "1.20.4": "https://api.papermc.io/v2/projects/paper/versions/1.20.4/builds/499/downloads/paper-1.20.4-499.jar",
    "1.20.2": "https://api.papermc.io/v2/projects/paper/versions/1.20.2/builds/318/downloads/paper-1.20.2-318.jar",
    "1.20.1": "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/196/downloads/paper-1.20.1-196.jar",
    "1.20": "https://api.papermc.io/v2/projects/paper/versions/1.20/builds/17/downloads/paper-1.20-17.jar",
    "1.19.4": "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar",
    "1.19.3": "https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/448/downloads/paper-1.19.3-448.jar",
    "1.19.2": "https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/307/downloads/paper-1.19.2-307.jar",
    "1.19.1": "https://api.papermc.io/v2/projects/paper/versions/1.19.1/builds/111/downloads/paper-1.19.1-111.jar",
    "1.19": "https://api.papermc.io/v2/projects/paper/versions/1.19/builds/81/downloads/paper-1.19-81.jar",
    "1.18.2": "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar",
    "1.18.1": "https://api.papermc.io/v2/projects/paper/versions/1.18.1/builds/216/downloads/paper-1.18.1-216.jar",
    "1.18": "https://api.papermc.io/v2/projects/paper/versions/1.18/builds/66/downloads/paper-1.18-66.jar",
    "1.17.1": "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar",
    "1.17": "https://api.papermc.io/v2/projects/paper/versions/1.17/builds/79/downloads/paper-1.17-79.jar",
    "1.16.5": "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar",
    "1.16.4": "https://api.papermc.io/v2/projects/paper/versions/1.16.4/builds/416/downloads/paper-1.16.4-416.jar",
    "1.16.3": "https://api.papermc.io/v2/projects/paper/versions/1.16.3/builds/253/downloads/paper-1.16.3-253.jar",
    "1.16.2": "https://api.papermc.io/v2/projects/paper/versions/1.16.2/builds/189/downloads/paper-1.16.2-189.jar",
    "1.16.1": "https://api.papermc.io/v2/projects/paper/versions/1.16.1/builds/138/downloads/paper-1.16.1-138.jar",
    "1.15.2": "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar",
    "1.15.1": "https://api.papermc.io/v2/projects/paper/versions/1.15.1/builds/62/downloads/paper-1.15.1-62.jar",
    "1.15": "https://api.papermc.io/v2/projects/paper/versions/1.15/builds/21/downloads/paper-1.15-21.jar",
    "1.14.4": "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar",
    "1.14.3": "https://api.papermc.io/v2/projects/paper/versions/1.14.3/builds/134/downloads/paper-1.14.3-134.jar",
    "1.14.2": "https://api.papermc.io/v2/projects/paper/versions/1.14.2/builds/107/downloads/paper-1.14.2-107.jar",
    "1.14.1": "https://api.papermc.io/v2/projects/paper/versions/1.14.1/builds/50/downloads/paper-1.14.1-50.jar",
    "1.14": "https://api.papermc.io/v2/projects/paper/versions/1.14/builds/17/downloads/paper-1.14-17.jar",
    "1.13.2": "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar",
    "1.13.1": "https://api.papermc.io/v2/projects/paper/versions/1.13.1/builds/386/downloads/paper-1.13.1-386.jar",
    "1.13": "https://api.papermc.io/v2/projects/paper/versions/1.13/builds/173/downloads/paper-1.13-173.jar",
    "1.13-pre7": "https://api.papermc.io/v2/projects/paper/versions/1.13-pre7/builds/12/downloads/paper-1.13-pre7-12.jar",
    "1.12.2": "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar",
    "1.12.1": "https://api.papermc.io/v2/projects/paper/versions/1.12.1/builds/1204/downloads/paper-1.12.1-1204.jar",
    "1.12": "https://api.papermc.io/v2/projects/paper/versions/1.12/builds/1169/downloads/paper-1.12-1169.jar",
    "1.11.2": "https://api.papermc.io/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar",
    "1.10.2": "https://api.papermc.io/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar",
    "1.9.4": "https://api.papermc.io/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar",
    "1.8.8": "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar"
    }

# Fonction pour télécharger le fichier .jar du serveur Minecraft
def download_server(version):
    versions = get_versions()
    if version in versions:
        url = versions[version]
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            if not os.path.exists("MCserver"):
                os.makedirs("MCserver")
            server_file_path = os.path.join("MCserver", "server.jar")
            with open(server_file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            messagebox.showinfo("Download Completed", "jarfile saved !")
            setup_server()
        else:
            messagebox.showerror("Error", "Server mabye down")
    else:
        messagebox.showerror("Error", "This is not a version x)")

# Fonction pour configurer les fichiers nécessaires (EULA et server.properties)
def setup_server():
    with open("MCserver/eula.txt", "w") as eula_file:
        eula_file.write("eula=false\n")
    
    messagebox.showinfo("Steps", "1. Open eula.txt (On the MCserver folder) and turn 'eula=false' to 'eula=true'.\n"
                                          "2. Press Launch server on the app.")
    start_button.pack()
    # Masquer la console au début
    console_text.pack_forget()  # On masque la zone de texte pour la console

# Fonction pour lancer le serveur après l'acceptation de l'EULA
def start_server():
    eula_file_path = "MCserver/eula.txt"
    if os.path.exists(eula_file_path):
        with open(eula_file_path, "r") as eula_file:
            content = eula_file.read()
            if "eula=true" not in content:
                messagebox.showwarning("Alerte", "You need to accept the eula\n"
                                                 "eula.txt >>> 'eula=false' to 'eula=true'.")
                return
    else:
        messagebox.showerror("Erreur", "Cant find eula.txt, do you deleted it?")
        return
    
    # Lancer le serveur dans un thread séparé
    current_dir = os.path.dirname(os.path.realpath(__file__))
    mcserver_dir = os.path.join(current_dir, "MCserver")
    
    if os.path.exists(mcserver_dir) and os.path.isfile(os.path.join(mcserver_dir, "server.jar")):
        try:
            # Lancer le serveur sans fenêtre de CMD
            process = subprocess.Popen(
                ["java", "-jar", "server.jar", "nogui"], 
                cwd=mcserver_dir, 
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, text=True, bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW  # Cacher la fenêtre de CMD
            )
            # Lancer un thread pour mettre à jour la console en arrière-plan
            threading.Thread(target=update_console, args=(process,), daemon=True).start()
            messagebox.showinfo("Server info", "Server started!")
            # Sauvegarder le processus pour envoyer des commandes plus tard
            global server_process
            server_process = process
        except Exception as e:
            messagebox.showerror("Error", f"Server launch failed : {e}")
    else:
        messagebox.showerror("Error", "Cant find server.jar")

# Fonction pour mettre à jour la console avec les logs du serveur en arrière-plan
def update_console(process):
    while True:
        output = process.stdout.readline()
        if output:
            # Afficher les logs dans la console si nécessaire, sinon les ignorer
            pass  # Pas d'affichage dans l'interface graphique

        # Vérification si le processus a terminé
        if process.poll() is not None:
            break  # Arrêter quand le processus est terminé

# Fonction pour envoyer des commandes au serveur
def send_command():
    command = command_entry.get() + "\n"
    if server_process:
        server_process.stdin.write(command)
        server_process.stdin.flush()
    command_entry.delete(0, tk.END)  # Effacer le champ de saisie

# Interface utilisateur
root = tk.Tk()
root.title("Minecraft Server Setup")
root.geometry("800x600")

# Sélection de la version de Minecraft
ttk.Label(root, text="Select a minecraft version :").pack()
version_entry = ttk.Combobox(root, values=list(get_versions().keys()))
version_entry.pack()

# Bouton pour télécharger le serveur
ttk.Button(root, text="Download and setup", command=lambda: download_server(version_entry.get())).pack()

# Champ pour entrer des commandes
command_entry = ttk.Entry(root, width=50)
command_entry.pack()

# Bouton pour envoyer la commande
ttk.Button(root, text="Send command to server", command=send_command).pack()

# Bouton pour démarrer le serveur (après acceptation de l'EULA)
start_button = ttk.Button(root, text="Start the server", command=start_server)
start_button.pack_forget()  # Cacher ce bouton au début

# Exécution de l'application
root.mainloop()
