import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
cx = os.getenv('CX')
key = os.getenv('KEY')

from convertor import convertor

def getLinkFromResult(result):
    if(result):
        return result.get("link")
    return ""

def googleSearch(search):
    GOOGLE_SEARCH_API_URL="https://www.googleapis.com/customsearch/v1"
    params = { 
        "key" : key,
        "cx" : cx,
        "q" : search,
        "searchType" : "image",
        "num": 5
    }
    with requests.session() as c:
        response = requests.get(GOOGLE_SEARCH_API_URL, params=params)
        try:
            searchResults = response.json()
            
        except BaseException as error:
            print("An exception occurred : {}".format(error))

        # if quota exceeded
        if(searchResults.get('error')):
            return str(searchResults.get('error').get('message'))

        return searchResults.get('items')

def formatSearch(googleSearchResult):
    if(isinstance(googleSearchResult, str)):
        print(googleSearchResult)
        return

    try:
        imageLinks = list(map(getLinkFromResult, googleSearchResult))
    except BaseException as error:
        print("An exception occurred : {}".format(error))
        return []

    # convert to string
    return convertor(imageLinks)

def googleImageSearch(search):
    return formatSearch(googleSearch(search))

# test getLinkFromResult - PASS
# sampleResult = {'title': 'some title', 'link': "the link"}
# print(getLinkFromResult(sampleResult))

# test googleSearch - PASS
# print(
#     formatSearch(
#         googleSearch("boy")
#     )
# )