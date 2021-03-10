import json
from flask import Flask, jsonify
from datos_server import principal, servername, fecha_servidor

app = Flask(__name__)

@app.route('/principal')
def getPrincipal():

	crear_archivo()

	return jsonify({"message": f"Servidor {servername()} analizado"})

def crear_archivo():

 	with open(f'<{servername()}>_<{fecha_servidor()}>.txt', 'w') as archivo_salida:
 		salida = principal()
 		json.dump(salida, archivo_salida)


@app.route('/principal', methods=['POST'])
def addPrincipal(): 
	return 'received'

if __name__ == '__main__':
	app.run(debug=True, port=4000)
	
