from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/estado_boton', methods=['GET','POST'])
def recibir_estado():
    try:
        data = request.get_json()
        estado = data.get('estado')
        
        if estado not in ['HIGH', 'LOW']:
            return jsonify({'error': 'Valor de estado no válido'}), 400
            
        print(f"Estado del botón recibido: {estado}")
        
        return jsonify({'mensaje': 'Estado recibido correctamente', 'estado': estado}), 200
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Error al procesar la solicitud'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)