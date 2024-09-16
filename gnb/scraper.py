# scraper.py
import requests
from bs4 import BeautifulSoup
from utils import get_soup

def get_job_listings(url):
    """
    Obtiene el listado de trabajos de la página principal.
    
    :param url: URL de la página principal de GetOnBoard
    :return: Lista de elementos HTML que representan trabajos
    """
    soup = get_soup(url)
    return soup.find_all("a", class_="gb-results-list__item")
