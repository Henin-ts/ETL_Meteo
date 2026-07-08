import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.getenv("API_KEY")
CITY = os.getenv("CITY")

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def extract():
    
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data
    raise Exception("Erreur lors de la récupération des données.")

