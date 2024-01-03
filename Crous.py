
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time


# Fonction pour envoyer un email
def send_email(subject, body):
    # Remplacez les champs suivants avec vos informations
    sender_email = "essayeh.rb@gmail.com"
    receiver_email = "rabie.essayeh@usmba.ac.ma"
    password = "xzmw pgeq dxvl qbma"
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)

        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

        print("Email envoyé avec succès!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Erreur d'authentification SMTP: {e}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")



# URL du site
url = "https://trouverunlogement.lescrous.fr/tools/32/search?bounds=-1.2419231_46.1908971_-1.111097_46.1331672"
# Fonction pour vérifier les logements CROUS
def check_crous_housing():
    # Récupération du contenu de la page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Vérification de la présence de logements CROUS
    # (Ceci est un exemple basique, vous devrez adapter cette partie en fonction de la structure réelle de la page)
    if "Aucun logement" not in soup.get_text():
        send_email("Nouveau logement CROUS disponible", "Un nouveau logement CROUS est disponible sur le site.\n\n"+ url)
        return True
    else:
        print("Pas encore")
        return False
    
print("Start")
while not check_crous_housing():
    check_crous_housing()
    time.sleep(60)
    

