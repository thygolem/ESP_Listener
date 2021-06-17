a = 0
b = None
s3 = "{'10:00:00:00:00:01' : ['RSSI' : -56] }"
mac_address = s3[2:19]
rssi = int(s3[33:36])
int(rssi)

print(mac_address)
print(rssi)
print("- - - - - - - - - - - - - - - - - - - - - -")


if mac_address == "10:00:00:00:00:01" :
    print('Uno está presente')
    if rssi < -55:
        b = True
        print(b)
else:
    print('MAL \n')
#print(a)
#print(b)
s3.find("RSSI")
if s3.count("RSSI") <= 3:
    print("ON")
else:
    print("OFF")



