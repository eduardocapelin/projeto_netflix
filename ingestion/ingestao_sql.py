import schedule
import time
import kagglehub
import shutil
import os

def baixar_netflix():
    path = kagglehub.dataset_download("shivamb/netflix-shows")
    csv_path = os.path.join(path, "netflix_titles.csv")
    destino = os.path.join(os.getcwd(), "netflix_titles.csv")
    shutil.copy(csv_path, destino)
    print("Arquivo atualizado em:", destino)

schedule.every().day.at("09:00").do(baixar_netflix)

while True:
    schedule.run_pending()
    time.sleep(60)