import time

status = True
zone = "B/F/Z"
while status == True:
    t = time.strftime('%H:%M:%S')
    segundos = int(t[6:9])
    print (segundos)
    time.sleep(1)
    if segundos % 2 == 0:
        zone = "B/Z/Y"
        print (zone)
    else:
        zone = "B/Z/X"
        print (zone)



 