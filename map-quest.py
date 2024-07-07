import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "yXjrmLQv87wdB0S7DjhUUAkiblzKWuQ2"
while True:
   orig = input("Lugar de Origen: ")
   if orig == "s":
    break
   dest = input("Lugar de Destino: ")
   if dest == "s":
    break
   route_type = input("Tipo de transporte (fastest, shortest, pedestrian, bicycle, multimodal): ")
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest, "for":route_type})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
        print("API Status: " + str(json_status) + " = Llamada de ruta exitosa.\n")
        print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
        print("Millas:           " + str("{:.2f}".format(json_data["route"]["distance"])))
        print("Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        for step in json_data["route"]["legs"][0]["maneuvers"]:
            print((step["narrative"]))
    