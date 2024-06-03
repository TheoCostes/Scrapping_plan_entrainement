
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Initialiser le navigateur
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://app.campus.coach/auth/signin")

# Localiser et remplir les champs de connexion
username_field = driver.find_element(By.NAME, "email")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys("theocostes77@gmail.com")
password_field.send_keys("76d!XCd&8XHpiP!T")

# Soumettre le formulaire
password_field.send_keys(Keys.RETURN)

# Attendre la redirection et s'assurer que la connexion est établie
time.sleep(5)  # Ajuster selon la rapidité du site

# Naviguer vers la page des séances et récupérer les noms
driver.get("https://app.campus.coach/")

# Attendre que la page soit complètement chargée
driver.implicitly_wait(10)  # ou utilisez WebDriverWait pour des attentes explicites

# Extraire le contenu HTML de la page
page_source = driver.page_source

# Fermer le navigateur
driver.quit()

# Utiliser BeautifulSoup pour parser le contenu HTML
soup = BeautifulSoup(page_source, 'html.parser')

# Trouver tous les éléments avec des classes
elements_with_classes = soup.find_all(class_=True)

# Extraire les classes uniques
classes = set()
for element in elements_with_classes:
    class_list = element.get('class')
    if "campus-ds__Wrapper-sc-niysmc-4" in class_list and "felyqZ" in class_list and len(class_list) <= 2:
        print(element.h3)

