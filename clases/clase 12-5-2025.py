import requests

respuesta = requests.get('https://www.elchat.com/paises/argentina.html')
print("codigo", respuesta.status_code)