# api.py
from flask import jsonify, request
from main import main
from utils import get_cities_weather_data
from weather_api import get_cities_weather_data

@main.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'Debe proporcionar el nombre de una ciudad.'}), 400

    weather_data = get_cities_weather_data(city)

    if not weather_data:
        return jsonify({'error': 'No se pudo obtener los datos climáticos para la ciudad proporcionada.'}), 404

    return jsonify(weather_data), 200

if __name__ == '__main__':
    main.run()