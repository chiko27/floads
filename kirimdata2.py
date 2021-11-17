import requests
import random
import time


url = 'http://127.0.0.1:5000/database'
i = 0
while(1):
    ikan = ["Euthynnus affinis","Katsuwonus pelamis"]
    spesies = random.choice(ikan)  
    Total = "SELECT spesies,count(*) AS Total FROM spesies_ikan GROUP BY spesies"
     
    myobj = {'species': spesies, 'amount': Total}

    # -------kirim data ke server
    # -------------------------------------------------
    x = requests.post(url, data=myobj)
    print(x.text)
    time.sleep(1)
    i = i+1

