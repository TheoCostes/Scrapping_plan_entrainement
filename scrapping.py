
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv('PASSWORD')
email = os.getenv('EMAIL')


# Initialiser le navigateur
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://app.campus.coach/auth/signin")

# Localiser et remplir les champs de connexion
username_field = driver.find_element(By.NAME, "email")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys(email)
password_field.send_keys(password)

# Soumettre le formulaire
password_field.send_keys(Keys.RETURN)

# Attendre la redirection et s'assurer que la connexion est établie
time.sleep(20)  # Ajuster selon la rapidité du site

# Naviguer vers la page des séances et récupérer les noms
driver.get("https://app.campus.coach/")

# Attendre que la page soit complètement chargée
driver.implicitly_wait(20)  # ou utilisez WebDriverWait pour des attentes explicites

# Extraire le contenu HTML de la page
page_source = driver.page_source

# Fermer le navigateur
driver.quit()


# Utiliser BeautifulSoup pour parser le contenu HTML
soup = BeautifulSoup(page_source, 'html.parser')

sessions = soup.find_all('div', {'data-testid': 'session-card'})

print(len(sessions))

session_data = []

for session in sessions:
    title_element = session.find('h3', {'class': 'campus-ds__HeadingItem-sc-niysmc-0'}) 
    duration_element = (
        session
        .find('div', {'class': 'campus-ds__Wrapper-sc-niysmc-4 iyQsnC'})
        .find('p', {'class': 'campus-ds__TextElement-sc-niysmc-1 dLqUiH'})
    )
    print(duration_element)
    duration = duration_element.get_text(strip=True) if duration_element else "Durée non trouvée"
    
    distance_element = (
        session
        .find('div', {'class': 'campus-ds__Wrapper-sc-niysmc-4 jPXRku'})
        .find('p', {'class': 'campus-ds__TextElement-sc-niysmc-1 dLqUiH'})
    )
    distance = distance_element.get_text(strip=True) if distance_element else "Distance non trouvée"

    title = title_element.get_text(strip=True) if title_element else "Titre non trouvé"
    # duration = duration_element.get_text(strip=True) if duration_element else "Durée non trouvée"
    # distance = distance_element.get_text(strip=True) if distance_element else "Distance non trouvée"
    
    session_data.append({
        'title': title,
        'duration': duration,
        'distance': distance
    })
    print("===")

# Afficher les résultats
print("Informations des sessions:")
for session in session_data:
    print(f"Nom: {session['title']}, Durée: {session['duration']}, Distance: {session['distance']}")