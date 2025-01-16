from flask import Flask, jsonify, request
from planet_calculator import PlanetCalculator

app = Flask(__name__)
calculator = PlanetCalculator()

@app.route('/planets', methods=['GET'])
def get_planets():
    return jsonify(calculator.planets)

@app.route('/add_planet', methods=['POST'])
def add_planet():
    data = request.get_json()
    name = data['name']
    habitability = data['habitability']
    theoretical = data.get('theoretical', False)
    calculator.add_planet(name, habitability, theoretical)
    return jsonify({"message": "Planet added successfully"})

@app.route('/delete_planet', methods=['DELETE'])
def delete_planet():
    data = request.get_json()
    name = data['name']
    result = calculator.delete_manual_planet(name)
    return jsonify({"message": result})

@app.route('/habitability_ratios', methods=['GET'])
def habitability_ratios():
    ratios = calculator.calculate_habitability_ratios()
    return jsonify({"ratios": ratios})

if __name__ == '__main__':
    app.run(debug=True)
