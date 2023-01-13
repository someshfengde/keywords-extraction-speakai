import logging.config
from pythonjsonlogger import jsonlogger
from flask_restful import Api, Resource
from flask import Flask

# API
from api.api_component import KeywordExtractionComponent

# Logger Configuration
logging.config.fileConfig('logging.ini')
logger = logging.getLogger('speakLogger')

Version = '1.0.000'

application = Flask(__name__)
api = Api(application)

class CheckHealth(Resource):
    @staticmethod
    def get():
        return 'Server is working! Version ' + Version

api.add_resource(CheckHealth, '/health')

# TODO: Add API Endpoint and Change component name
api.add_resource(KeywordExtractionComponent, '/keywords')

if __name__ == '__main__':
    PORT = 5000
    DEBUG_MODE = True
    logger.info('Server is running. ' + Version)
    application.run(port=PORT, debug=DEBUG_MODE)
