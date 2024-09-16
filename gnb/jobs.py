# job_details.py
from bs4 import BeautifulSoup
from utils import get_soup, clean_text

def get_job_details(job):
    """
    Extrae los detalles de un trabajo específico.
    
    :param job: Elemento HTML que representa un trabajo
    :return: Diccionario con los detalles del trabajo
    """
    title = get_title(job)
    company = get_company(job)
    location = get_location(job)
    description = get_description(job)
    
    return {
        "Título": title,
        "Compañía": company,
        "Ubicación": location,
        "Descripción": description
    }

def get_title(job):
    title_element = job.find("h4", class_="gb-results-list__title").find("strong")
    return clean_text(title_element.text) if title_element else "Título no disponible"

def get_company(job):
    company_element = job.find("div", class_="size0").find("strong")
    return clean_text(company_element.text) if company_element else "Compañía no disponible"

def get_location(job):
    location_element = job.find("span", class_="location")
    if location_element:
        location_text = location_element.get_text(separator="\n", strip=True)
        return location_text.split('\n')[0].strip() if location_text else "Ubicación no disponible"
    return "Ubicación no disponible"

def get_description(job):
    details_url = job['href']
    if not details_url.startswith("http"):
        details_url = "https://www.getonbrd.com" + details_url
    
    details_soup = get_soup(details_url)
    job_body_element = details_soup.find("div", id="job-body")
    
    if job_body_element:
        description_parts = job_body_element.find_all("div", class_="gb-rich-txt")
        return "\n\n".join([clean_text(part.get_text()) for part in description_parts])
    return "Descripción no disponible"
