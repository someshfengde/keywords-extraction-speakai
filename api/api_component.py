from flask import jsonify, request
from flask_restful import Resource
import logging

# adding pandas (DEBUG LOCAL ONLY)
import pandas as pd 


from utils.requests import post_request
logger = logging.getLogger('speakLogger')

def get_keywords_frequency(semantic_search_dict, top_k = 10):
    """
    This function will return the keywords frequency from the source
    
    Inputs:
        :param source: source data in python dictionary (good for local testing as well as API ) 
        :param top_k: top k keywords to be returned default is 10) 

    Output: 
        :return: keywords frequency in python dictionary    
    """
    print("semantic search json is:")
    text_array = [] 
    for key in semantic_search_dict['transcript']:
        text_array.append(key['text'])
    # calculating the top k keywords from transcription object using python flask 
    
    # finding the frequency of each word
    wordfreq = {}
    total_scentence = " ".join(text_array)

    # finding the frequency of each word
    for y in total_scentence.split():
        wordfreq[y] = total_scentence.count(y)
    
    # sorting the frequency of each word
    sorted_wordfreq = dict(sorted(wordfreq.items(), key=lambda x: x[1], reverse=True))

    top_k_dict = {} 
    for i in range(top_k):
        top_k_dict[list(sorted_wordfreq.keys())[i]] = list(sorted_wordfreq.values())[i]
    
    output_dict = []
    for idx, (key, val) in enumerate(top_k_dict.items()):
        # finding the instances in which key appeared
        tot_instances = []
        for k in semantic_search_dict['transcript']:
            if key in k['text']:
                tot_instances.extend(k['instances'])
        output_dict.append({"instances":tot_instances,
                            'id':idx, 
                            "name":key, 
                            })

    return {"keywords":output_dict}

class KeywordExtractionComponent(Resource):
    @staticmethod
    def get(): 
        semantic_data = dict(pd.read_json("data/Semantic Search.json"))
        print(semantic_data)
        response = get_keywords_frequency(semantic_data)
        return jsonify(response)

    @staticmethod
    def post():
        print('asdkfl;ajsdl;fj')
        # posted_data = dict(request.get_json())

        # requestId = posted_data['requestId']
        # companyId = posted_data['companyId']
        # userId = posted_data['userId']
        

        # getting the locally downloaded JSON data from 
        source = dict(pd.read_json("data/Semantic Search.json")) # posted_data['source']
        # callbackUrl = posted_data['callbackUrl']

        # logger.info("Request for _______", extra={
        #             'requestId': requestId, 'userId': userId, 'companyId': companyId, 'callbackUrl': callbackUrl})

        result = get_keywords_frequency(source)
        response = jsonify(result)

        # if callbackUrl assigned then make a call and send results
        # if callbackUrl:
        #     post_request(callbackUrl, result)

        # logger.info("Finish: Request for _______", extra={
        #     'requestId': requestId, 'userId': userId, 'companyId': companyId})
        return response
