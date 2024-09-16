# main.py
import pandas as pd
from scraper import get_job_listings
from jobs import get_job_details

def main():
    # URL principal de GetOnBoard
    url = "https://www.getonbrd.com/"
    
    # Obtener listado de trabajos
    job_listings = get_job_listings(url)
    
    # Obtener detalles de cada trabajo
    jobs = [get_job_details(job) for job in job_listings]
    
    # Crear DataFrame y exportar a CSV
    df = pd.DataFrame(jobs)
    df.to_csv("trabajos.csv", index=False)
    print("Datos exportados a trabajos.csv")

if __name__ == "__main__":
    main()
