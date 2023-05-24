from flask import Flask, request, Blueprint
from flask_restful import Resource, Api

rocket_api = Blueprint('rocket_api', __name__,
                   url_prefix='/api/rocket')
api = Api(rocket_api)

class RocketLaunch(Resource):
    def post(self):
        velocity = request.json['velocity']
        result = launch_rocket(velocity)
        return {'result': result}
    
def launch_rocket(velocity):
    # Constants
    GRAVITY = 9.8  # Acceleration due to gravity in m/s^2
    EARTH_RADIUS = 6371000  # Radius of the Earth in meters
    ORBITAL_VELOCITY = 7800  # Approximate orbital velocity in m/s
    
    # Calculate the time of flight and maximum height of the rocket
    time_of_flight = (2 * velocity * (velocity * (2 * GRAVITY * EARTH_RADIUS) ** 0.5)) / (GRAVITY * (2 * GRAVITY * EARTH_RADIUS) ** 0.5)
    max_height = (velocity ** 2) / (2 * GRAVITY)
    
    # Determine if the rocket reaches orbit
    if velocity >= ORBITAL_VELOCITY:
        return 'Rocket successfully reached orbit!'
    elif max_height > EARTH_RADIUS:
        return 'Rocket reached a maximum height but failed to reach orbital velocity.'
    else:
        return 'Rocket failed to reach orbit.'
    
api.add_resource(RocketLaunch, '/rocket')