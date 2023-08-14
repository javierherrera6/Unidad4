import requests
from login import obtener_token

def get_networdevicecount():
    token = obtener_token()
    url = "http://127.0.0.1:58000/api/v1/network-device/count"

    headers = {
        "X-Auth-token": token
    }

    respuesta = requests.get(url, headers=headers)
    device_count = respuesta.json()["response"]

    return device_count

def main():
    device_count = get_networdevicecount()

    # Crear o sobrescribir un archivo de texto con el resultado
    with open("device_count.txt", "w") as f:
        f.write("Cantidad de dispositivos en la red: " + str(device_count))
    print("El total de dispositivos en la red es: " + str(device_count) + ". El resultado fue guardado en device_count.txt")

if __name__ == "__main__":
    main()