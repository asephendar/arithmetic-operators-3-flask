from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/tambahan', methods=['POST'])
def Addition():
    a = request.json['a']
    b = request.json['b']
    
    hasil = a + b
    return jsonify({"results" : hasil})

@app.route('/kurang', methods=['POST'])
def Subtraction():
    a = request.json['a']
    b = request.json['b']
    
    hasil = a - b
    return jsonify({"results" : hasil})

@app.route('/kali', methods=['POST'])
def Multiplication():
    a = request.json['a']
    b = request.json['b']
    
    perkalian = a * b
    return jsonify({"results" : perkalian})

@app.route('/bagi', methods=['POST'])
def Division():
    a = request.json['a']
    b = request.json['b']
    
    pembagian = a / b
    return jsonify({"results" : pembagian})

if __name__ == '__main__':
    app.run(debug=True)