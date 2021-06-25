import time

helpButton = "['10:00:00:00:00:01' : {'HELP' : True},]"
help = bool(helpButton[33:37])
print(help)

if help == True:
    print("Inicializando asistente, comunicando por telegram")
    time.sleep(2.5)
    print("""           
                            ¿Qué necesitas?
                1) Operario\U0001f600        3) Herramienta\U0001F9F0
                2) Asistente\U0001F916       4) Otro
                             Elige número
                """)
    opcion = input()
    if (opcion == "1") or (opcion == "Operario"):
        print("Enviando operario\U0001f600")
    elif (opcion == "2") or (opcion == "Asistente"):
        print("Iniciando asistente\U0001F916")
    elif (opcion == "3") or (opcion == "Herramienta") :
        print("Enviando caja de Herramientas\U0001F9F0")
    elif (opcion == "4") or (opcion == "Otro"):
        time.sleep(0.5)
        print("  1 \U0001f600")
        time.sleep(0.5)
        print("   2 \U0001F916")
        time.sleep(0.5)
        print("     3 \U0001F9F0")
        time.sleep(0.5)

# debe haber una Db con las identificaciones de las ayudas
# deberá aparecer un selector de herramientas o tipo de asistencia en el chat de telegram
# el objetivo es comunicar directamente con otros operarios disponibles
# ó hablar con una máquina de almacenaje automático para que prepare las herramientas
# las herramientas se llevarán automáticamente a la zona donde se está llevando a cabo la operación
# el objetivo es tmabién aprovechar este sistema para competir con empresas de automatización de envíos
# yendo un paso por delante para proteger a los empleados