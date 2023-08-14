import requests
from login import obtener_token


def get_users():
    token = obtener_token()
    url = "http://127.0.0.1:58000/api/v1/user"

    headers = {
        "X-Auth-token": token
    }

    respuesta = requests.get(url, headers=headers)
    respuesta_json = respuesta.json()

    return respuesta_json


if __name__ == "__main__":
    respuesta = get_users()
    users = respuesta["response"]

    for user in users:
        username = user["username"]
        roles = user["authorization"][0]["role"]
        password = user["password"]

        print(f"Usuario: {username}, Contraseña: {password} Rol: {roles}")