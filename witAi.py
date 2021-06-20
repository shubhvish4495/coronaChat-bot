from wit import Wit
import json
import configurations as conf
import getCovidData

def checkConfidenceRange(confidence):
    if confidence >= 0.80:
        return True
    return False

def entryCovidChatBot(message):
    client = Wit(conf.WIT_ACCESS_TOKEN)
    resp = client.message(message)
    print("---------------\n")
    print(resp)
    print("--------------\n")
    # if (resp["entities"]):
    #     print(resp["entities"])
    #     try:
    #         for m in resp["entities"]["intent"]:
    #             if m["value"] == conf.INTENT_CORONA and checkConfidenceRange(m["confidence"]):
    #                 print()
    #             else:
    #                 return ("Sorry I can answer queries only for new corona cases!!!")
    #             for z in resp["entities"]["location"]:
    #                 if checkConfidenceRange(z["confidence"]):
    #                     # print("Fetching data for " + str(z["value"]).title() +"........")
    #                     response = getCovidData.getCovidDataForDistrict( str(z["value"]).title())
    #                     return ("\nTotal Active cases are: "+ str(response["active"]) + "\n\nConfirmed cases are: " + str(response["confirmed"])+"\n")
    #                 else:
    #                     return ("Can you check the name of district. I am still learning!!!")
    #     except KeyError:
    #         return ("I will need the district name to fetch data")
    try:
        for intent in resp["intents"]:
            if intent["name"] == conf.INTENT_CORONA and checkConfidenceRange(intent["confidence"]):
               locationEntity = resp["entities"]["wit$location:location"]
               for singleLocationEntity in locationEntity:
                   if (checkConfidenceRange(singleLocationEntity["confidence"])):
                       districtName = singleLocationEntity["body"]
                       response = getCovidData.getCovidDataForDistrict(str(districtName).title())
                       return ("\nTotal Active cases are: "+ str(response["active"]) + "\n\nConfirmed cases are: " + str(response["confirmed"])+"\n")
                   else:
                       return ("I will require proper district name to operate")
            else:
                return ("Sorry can answer queries realted to Covid-19 only!!")
        return ("Sorry can answer queries realted to Covid-19 only!!")
    except Exception:
        return ("Sorry am in development phase, Please recheck the query/district name provided to me")

