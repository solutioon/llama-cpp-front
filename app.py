from flask import Flask, render_template, request
import requests
import json
#we import waitress here. 
from waitress import serve

app = Flask(__name__)

mensajes = []
texto =""

#VARIABLES PARA LLAMADA API
tokens=128

@app.route('/nueva', methods=['GET', 'POST'])
def nueva():
    mensajes = []
    # Realizar la acción deseada con el mensaje
    # ...

    #return "Acción realizada con éxito"
    return render_template('index.html', mensajes=mensajes)


@app.route('/', methods=['GET', 'POST'])
def reordenar():
    if request.method == 'POST':
        texto = request.form['texto']
        # Definir el JSON a enviar
        data = {
        "prompt": "\n\n### Instructions:\n"+texto+"\n\n### Response:\n",
        "stop": [
          "\n",
          "###"
          ],
        "max_tokens": tokens,
        "stream": 0
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
        print("Mandamos:", json_data)
        # Obtener la respuesta de la API
        if response.status_code == 200:
            # La solicitud se realizó correctamente
            response_data = response.json()
            print("Respuesta:",response_data)
        else:
            # Hubo un error en la solicitud
            print("Error:", response.status_code)
            response_data = "Error:", response.status_code
        
        #data = json.loads(response_data) 
        texto_reordenado = response_data["choices"][0]["text"]
        #texto_reordenado = "hola"
        mensajes.append({'texto': texto, 'reordenado': texto_reordenado})
    return render_template('index.html', mensajes=mensajes)

if __name__ == '__main__':
    #app.run(debug=True)
    serve(app, host='0.0.0.0', port=5001)
