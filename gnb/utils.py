# utils.py
import requests
from bs4 import BeautifulSoup

def get_soup(url):
    """
    Obtiene el objeto BeautifulSoup de una URL dada.
    
    :param url: URL a scrapear
    :return: Objeto BeautifulSoup
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, "html.parser")

def clean_text(text):
    """
    Limpia el texto eliminando espacios en blanco extra y saltos de línea.
    
    :param text: Texto a limpiar
    :return: Texto limpio
    """
    return ' '.join(text.strip().split())
