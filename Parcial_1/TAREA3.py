from pynput.keyboard import Key, Listener
from datetime import datetime
import time

# Variables globales
contador_eventos = 0
tiempo_anterior = None
archivo_log = "tarea_3.txt"

def procesar_evento(accion, key):
    global contador_eventos, tiempo_anterior
    
    # Incrementa el número de evento
    contador_eventos += 1
    
    # Toma el tiempo exacto actual para calcular el delta_ms
    tiempo_actual = time.time()
    
    if tiempo_anterior is None:
        delta_ms = 0
    else:
        # Diferencia de tiempo en milisegundos
        delta_ms = int((tiempo_actual - tiempo_anterior) * 1000)
        
    tiempo_anterior = tiempo_actual
    
    # Genera la fecha y hora con el formato exacto: 2026-08-23T22:50:10.163-06:00
    fecha_hora = datetime.now().astimezone().isoformat(timespec='milliseconds')
    
    # Formato para la tecla (alfanumérica con comillas simples, especiales sin comillas)
    try:
        tecla_str = f"'{key.char}'"
    except AttributeError:
        tecla_str = f"{key}"
        
    # Construye la línea exactamente como en la imagen
    linea = f"{fecha_hora} | [{accion}] | evento_{contador_eventos:03d} | tecla={tecla_str} | delta_ms={delta_ms}\n"
    
    # Imprime en consola solo para que veas que está funcionando
    print(linea.strip())
    
    # Guarda en el archivo tarea_3.txt sin borrar lo anterior
    with open(archivo_log, "a", encoding="utf-8") as archivo:
        archivo.write(linea)

def on_press(key):
    procesar_evento("PRESS", key)

def on_release(key):
    # En tu imagen aparecen tanto PRESS como RELEASE. Si el profe te pidió que 
    # *estrictamente* solo aparezca cuando se presionó, puedes borrar o comentar 
    # la siguiente línea:
    procesar_evento("RELEASE", key)
# Imprime un mensaje para que sepas que ya arrancó
print("¡El programa está activo y escuchando! Presiona algunas teclas... (Presiona ESC para salir)")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()