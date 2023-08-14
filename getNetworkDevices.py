import requests
import csv
from login import obtener_token


def get_network_devices():
    token = obtener_token()
    url = "http://127.0.0.1:58000/api/v1/network-device"

    headers = {
        "X-Auth-token": token
    }

    respuesta = requests.get(url, headers=headers)
    respuesta_json = respuesta.json()

    return respuesta_json


def main():
    respuesta = get_network_devices()
    devices = respuesta["response"]

    # Crear o sobrescribir un archivo CSV
    with open("network_devices.csv", "w", newline="") as csvfile:
        fieldnames = ["Nombre de Host", "Tipo", "Dirección IP de Administración", "Número de Interfaces", "Plataforma",
                      "Versión de Software"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Escribir la fila de encabezados

        for device in devices:
            hostname = device["hostname"]
            device_type = device["type"]
            management_ip = device["managementIpAddress"]
            interface_count = device["interfaceCount"]
            platform = device["platformId"]
            software_version = device["softwareVersion"]

            writer.writerow({
                "Nombre de Host": hostname,
                "Tipo": device_type,
                "Dirección IP de Administración": management_ip,
                "Número de Interfaces": interface_count,
                "Plataforma": platform,
                "Versión de Software": software_version
            })  # Escribir los datos en el archivo CSV


if __name__ == "__main__":
    main()