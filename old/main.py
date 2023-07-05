from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route("/")
def home():
    return render_template("index.html")

# Ruta para procesar las consultas del chatbot
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Obtenemos la consulta del usuario
    user_query = request.form["user_query"]
    
    # TODO: aquí va el código para procesar la consulta y generar la respuesta del chatbot
    def get_bot_response(request):
      user_text = request.form['user_input']
    return user_text	    
    chatbot_response=get_bot_response(user_query)
    # Retornamos la respuesta en formato JSON
    return jsonify({"response": chatbot_response})

if __name__ == "__main__":
    app.run(debug=True)

