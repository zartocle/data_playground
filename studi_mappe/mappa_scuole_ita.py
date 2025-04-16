# Questo script legge un file csv contenente una serie di indirizzi e attraverso il servizio Nominatim (OpenStreetMap)
# recupera le coordinate GPS, facendone una lista che viene poi salvata in un file.
### TIENI PRESENTE CHE IN CASO DI LISTE LUNGHE, L'ESECUZIONE PUO' DURARE SVARIATE ORE ###
import os		# Interfaccia con il sistema operativo: RTFM QUA https://docs.python.org/3/library/os.html
from geopy import Nominatim     # Interfaccia con OpenStreetMaps
import folium                   # Servirà poi per creare la mappa
import pandas                   # Gestione del dataframe
from time import sleep          # Per far aspettare un attimo lo script tra una richiesta al server e l'altra
import logging                  # Non ancora usato - per gestire i log
import datetime as dt

logging.basicConfig(filename="log_mappatore_scuole.txt",
                level=logging.INFO,
                format='%(levelname)s: %(asctime)s %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S')


def ritornaora():
   return dt.datetime.now().strftime("%y-%m-%d %H:%M:%S")

# Importa il csv (OCCHIO. ALLA. CODIFICA. E' IMPORTANTE.)
myHome=os.getenv("HOME")        # Get the HOME dir: this syntax will work on all UNIX
os.chdir(myHome)        	# Set the WD
scuole=pandas.read_csv(myHome+'/python/EserciziPy/anagrafica_2.csv',sep=';',encoding='ISO-8859-1')

# Pulisci via i NaN, colonna per colonna:
scuole['indirizzo']=scuole['indirizzo'].fillna(" ")
scuole['cap']=scuole['cap'].fillna(" ")
scuole['comune']=scuole['comune'].fillna("Rijeka")
# Aggiungi campo indirizzo completo
scuole['ind_completo']=scuole['indirizzo']+' '+scuole['cap'] +' '+ scuole['comune'] + ' Italy'
scuole['ind_parziale']=scuole['cap'] +' '+ scuole['comune'] + ' Italy'

# COSI' SI SOSTITUISCE L'INDESIDERATO DA UNA COLONNA
#scuole['cap']=scuole['cap'].str.replace('-----','')
# ... ma più utile e' fregarsene e convertire tutto in formato numerico (fa sparire il rumore in automatico):
# scuole['cap']=pandas.to_numeric(scuole['cap'], errors='coerce') 
# Geocoding con Nominatim

locatore = Nominatim(user_agent='BudeTerence')  # sembra una cazzata, ma Nominatim vuole non user agent che non sia standard o ti sega
coord=[]
f=open('coordinate_scuole.txt','w+')
for cod_sc,ind_c,ind_p in zip(list(scuole.loc[4446:,'codice_scuola']),list(scuole.loc[4446:,'ind_completo']),list(scuole.loc[4446:,'ind_parziale'])):#zip(list(scuole['codice_scuola']),list(scuole['ind_completo']),list(scuole['ind_parziale'])):#
    while True: # Questo e' un modo bizzarro per fare "attendere" il programma in caso la connessione non vada: se geocode da' errore, except aspettera' 15 min. e poi riprovera'
        try:
            #print(ind_c)
            location = locatore.geocode(ind_c)    # Questo metodo richiede la connessione a nominatim
            if location is not None: # CONTROLLA CHE LOCATION SIA STATO INIZIALIZZATO CORRETTAMENTE
                #coord.append([location.latitude,location.longitude])
                f.write("["+ritornaora()+","+str(cod_sc)+",["+str(location.latitude) + ',' + str(location.longitude) + ']]\n')
                #print(location.latitude)
                #print(location.longitude)
            else:   # QUA USO DOPPIA VARIABILE: SE IND COMPLETO NON HA DATO ESITO, CAP + CITTA + ITALY COME FALLBACK
                try:
                    location = locatore.geocode(ind_p)
                    #coord.append([location.latitude,location.longitude])
                    f.write("["+ritornaora()+","+str(cod_sc)+",["+str(location.latitude) + ',' + str(location.longitude) + ']]\n')
                    #print(location.latitude)
                    #print(location.longitude)
                except:     # SE ANCHE COSI' NON SI QUAGLIA, APPICCICA LE COORDINATE DELL'IRREDENTISSIMA
                    #coord.append([45.3271752,14.4412309])
                    f.write("["+ritornaora()+","+str(cod_sc)+",["+str(45.3271752)+','+str(14.4412309)+']]\n')
                    #print('FIUME')
                    #print('FIUME')
            sleep(5)
        except:
            logging.warning("Connessione a Nominatim fallita: nuovo tentativo tra 15 minuti.")
            sleep(900)   # Aspetta 15 minuti
            continue	 # Riprova a connetterti (location.geocode)
        break

#print(coord)

f.close

# POI TRASFORMA IL CAMPO IND COMPLETO IN UNA LISTA E USA UN CICLO FOR PER TROVARE LAT/LON

# al che, appiccica il risultato al dataframe

