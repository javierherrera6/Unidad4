import requests
import json


# Función para obtener token
def obtener_token():
    url = "http://127.0.0.1:58000/api/v1/ticket"  # URL del endpoint para obtener el token

    # Datos de autenticación
    body = {
        "password": "PASSWORD",
        "username": "USERNAME"
    }

    # Encabezados para la solicitud HTTP
    headers = {
        "content-type": "application/json"
    }

    # Construcción de petición POST para obtener token
    requests.packages.urllib3.disable_warnings()  # Con esta línea deshabilitamos warnings
    respuesta = requests.post(url, data=json.dumps(body), headers=headers)  # Petición POST
    # print(respuesta.json()) # Imprime respuesta en formato JSON
    # print("Código de estado HTTP es: ", respuesta.status_code)
    respuesta_json = respuesta.json()  # Convertir la respuesta JSON a un diccionario de Python y guardar en variable
    token = respuesta_json["response"]["serviceTicket"]  # Acceder al campo "serviceTicket donde está el APIToken"

    return token  # Devuelve el token obtenido



# Llamar a la función para obtener el token
def main():
    token = obtener_token()
    print("El token es: " + token)


# Iniciar la función principal si se ejecuta el script directamente
if __name__ == "__main__":
    main()