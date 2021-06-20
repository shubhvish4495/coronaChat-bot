import requests
import configurations as conf
import json

resp = requests.get(url = conf.COVID_DATA_URL)

data = resp.json()

def getCovidDataForDistrict(cityName):
    for key in data:
        for keyD in data[key]["districtData"]:
            if keyD == cityName:
                return(data[key]["districtData"][keyD])
    return {}
    
