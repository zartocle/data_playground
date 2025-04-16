import json
import os
from difflib import get_close_matches

#os.chdir("python/")
jdata=json.load(open("python/data.json"))

def trovaparola(par):
    par = par.lower()
    if par in jdata.keys():
        return jdata[par]
    elif len(get_close_matches(par,jdata.keys())) > 0:
        yesorno = input("The word you were looking for e' SCANOSCIUTA. Intendevi forse %s ?" % get_close_matches(par,jdata.keys())[0] )
        if yesorno == "y":
            return jdata[get_close_matches(par,jdata.keys())[0]]
        else:
            return "Then I'm sorry, I don't have this."
    else:
        return "The word you're looking for in not nel dizionario della MMERDA"

palora = input("Che parola vuoi cercare? ")
print(trovaparola(palora))
