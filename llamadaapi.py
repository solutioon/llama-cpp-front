import requests
import json

# Definir el JSON a enviar
data = {
    "prompt": "\n\n### Instructions:\nWhat is the capital of France?\n\n### Response:\n",
    "stop": [
        "\n",
        "###"
    ]
}

# Convertir el JSON a formato de cadena
json_data = json.dumps(data)

# Establecer la URL de la API
url = "http://10.200.250.55:8000/v1/completions"

# Establecer las cabeceras (headers) necesarias, si las hubiera
headers = {
    "Content-Type": "application/json"
}

# Realizar la solicitud POST a la API con el JSON
response = requests.post(url, data=json_data, headers=headers)

# Obtener la respuesta de la API
if response.status_code == 200:
    # La solicitud se realizó correctamente
    response_data = response.json()
    print(response_data)
else:
    # Hubo un error en la solicitud
    print("Error:", response.status_code)
