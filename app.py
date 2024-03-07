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

if __name__ == '__main__':
    app.run(debug=True)