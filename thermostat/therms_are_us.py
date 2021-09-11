from flask import abort, Flask, json, request

api = Flask(__name__)

@api.route('/ThermsAreUs/api/v1.0/current-temp', methods = ['GET'])
def get_temp():
    with open('thermostat.json') as f:
        data = json.load(f)
        return '{"temp":' + str(data['temp']) +'}'

@api.route('/ThermsAreUs/api/v1.0/current-setpoint', methods = ['GET', 'PUT'])
def update_setpoint():
    if request.method == 'PUT':
        if not request.json:
            abort(400)
        if 'setpoint' not in request.json:
            abort(400)
        if not isinstance(request.json['setpoint'], (int, long, float)):
            abort(400)
        with open('thermostat.json') as f_read:
            data = json.load(f_read)
            data['setpoint'] = request.json['setpoint']
            with open('thermostat.json', 'w') as f_write:
                json.dump(data, f_write)
    with open('thermostat.json') as f_read:
        data = json.load(f_read)
        return '{"setpoint":' + str(data['setpoint']) + '}'

if __name__ == '__main__':
    api.run(debug = True, host = '0.0.0.0')
