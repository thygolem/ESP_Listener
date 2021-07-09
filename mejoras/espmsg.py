## PENDIENTE

# - - - - - RECOGER LOS MAC ADDRESS - - - - - -
# La intención es guardar en una variable el tipo de str que quiero usar:
# que es los 17 caracteres que vengan después de cada "mac":"
# El objetivo es filtrar el nombre de cada mac y ahorrar mensajes desde el ESP32
# Tras haberlo conseguido, lo suyo sería poder recoger los 29 caracteres posteriores para usar también el RSSI correspondiente
## PENDIENTE


esp = '{"timestamp":"2021-07-09T09:46:43Z","g_mac":"4C:11:AE:8B:4C:94","mac":"fa:04:ce:a4:90:e6","rssi":-94,"bleName":"","mac":"fb:04:ce:a4:90:e6","rssi":-94,"bleName":"","mac":"fc:04:ce:a4:90:e6","rssi":-94,"bleName":"","mac":"fd:04:ce:a4:90:e6","rssi":-94,"bleName":""}'
print("espOriginal: ", esp)
filtrado = esp.find("mac")
mac = esp[39:42]
mac_address = mac + " " + esp[45:62]
print(filtrado)
print(mac)
print(mac_address)

for i in esp:
    if i == mac_address:
        continue
    else:
        print(i, end = "mac")
