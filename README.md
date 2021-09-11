# Thermostat Simulator

A thermostat simulator that is designed like a REST API and built with Python and Flask. The current temperature and setpoint is stored in a JSON file. The thermostat sim accepts GET requests for the temperature and setpoint as well as PUT requests for the setpoint. AWS Alexa provides voice functionality for the thermostat simulator. Alexa relies on the AWS Lambda functions to send HTTP requests to the thermostat API.

## Screenshots

![get temp](https://github.com/awolffromspace/thermostat-sim/blob/master/screenshots/get_temp.png?raw=true)

![set setpoint](https://github.com/awolffromspace/thermostat-sim/blob/master/screenshots/set_setpoint.png?raw=true)
