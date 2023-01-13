from flask import jsonify, request
from flask_restful import Resource
import logging

from utils.requests import post_request
logger = logging.getLogger('speakLogger')

def component_logic(source):
    #########
    # TODO: ADD LOGIC HERE...
    #########
    return ''

class KeywordExtractionComponent(Resource):
    @staticmethod
    def post():
        posted_data = dict(request.get_json())

        requestId = posted_data['requestId']
        companyId = posted_data['companyId']
        userId = posted_data['userId']
        source = posted_data['source']
        callbackUrl = posted_data['callbackUrl']

        logger.info("Request for _______", extra={
                    'requestId': requestId, 'userId': userId, 'companyId': companyId, 'callbackUrl': callbackUrl})

        result = component_logic(source)
        response = jsonify(result)

        # if callbackUrl assigned then make a call and send results
        if callbackUrl:
            post_request(callbackUrl, result)

        logger.info("Finish: Request for _______", extra={
            'requestId': requestId, 'userId': userId, 'companyId': companyId})
        return response
