import requests
import random
import time
import string


url = 'http://127.0.0.1:5000/database'
i = 0
def id_kapal(size1, chars1=string.digits):
    return ''.join(random.choice(chars1) for x in range(size1))
def id_nelayan(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
while(1):
    kapal = ["GT.87/No.2512", "GT.60/No.2772", "GT.102/No.2484", "GT.55/No.1179", "GT.74/No.1641"]
    ikan = ["Euthynnus affinis","Katsuwonus pelamis"]
    lokasi = ["WPP 571","WPP 572","WPP 573","WPP 713","WPP 714","WPP 715","WPP 716","WPP 717", "WPP 718"]
    idk = id_kapal(4)
    idn = id_nelayan(8, "AEIOSUMA23")
    weight = random.uniform(120,170) 
    species = random.choice(ikan)  
    location = random.choice(lokasi)
     
    myobj = {'berat': weight, 'spesies': species, 'id_kapal' : idk, 'id_nelayan' : idn, 'lokasi': location}

    # -------kirim data ke server
    # -------------------------------------------------
    x = requests.post(url, data=myobj)
    print(x.text)
    time.sleep(1)
    i = i+1

