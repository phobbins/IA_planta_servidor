from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Lista para guardar las mediciones
datos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Actualizar estado manualmente
        idx = int(request.form["id"])
        nuevo_estado = request.form["estado"]
        datos[idx]["estado"] = nuevo_estado
        return redirect(url_for('index'))
    
    return render_template("index.html", datos=datos)

@app.route("/registrar", methods=["POST"])
def registrar():
    # Recibir datos de la ESP32
    contenido = request.json
    nueva_entrada = {
        "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "luz": contenido.get("luz"),
        "temperatura": contenido.get("temperatura"),
        "humedad": contenido.get("humedad"),
        "estado": ""
    }
    datos.append(nueva_entrada)
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
