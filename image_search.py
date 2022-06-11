import requests
import json
import os
from dotenv import load_dotenv

# to extract text from html
import lxml.html

load_dotenv()
cx = os.getenv('CX')
key = os.getenv('KEY')

from convertor import convertor

def getLinkFromResult(result):
    if(result):
        return result.get("link")
    return ""

def getDescriptionFromResult(result):
    if(result):
        htmlSnippet = result.get("htmlSnippet")
        extractedText = lxml.html.fromstring(htmlSnippet)
        return extractedText.text_content()
    return ""

def googleSearch(search, searchType="search_type_undefined", num=5):
    GOOGLE_SEARCH_API_URL="https://www.googleapis.com/customsearch/v1"
    params = { 
        "key" : key,
        "cx" : cx,
        "q" : search,
        "searchType" : searchType,
        "num": num
    }
    with requests.session() as c:
        response = requests.get(GOOGLE_SEARCH_API_URL, params=params)
        try:
            searchResults = response.json()
            # print(searchResults)

        except BaseException as error:
            print("An exception occurred : {}".format(error))

        # if quota exceeded
        if(searchResults.get('error')):
            raise Exception(str(searchResults.get('error').get('message')))

        return searchResults
        # return searchResults

def getImageLink(googleSearchResult):
    try:
        googleSearchResult = googleSearchResult.get("items")
    except BaseException as error:
        print("Exception in extracting image link : {}".format(error))
        return convertor([])

    try:
        imageLinks = list(map(getLinkFromResult, googleSearchResult))
    except BaseException as error:
        raise error

    # convert to string
    return convertor(imageLinks)

def getDescription(googleSearchResult):
    try:
        googleSearchResult = googleSearchResult.get("items")
    except BaseException as error:
        print("Exception in extracting HTML : {}".format(error))
        return ""

    try:
        htmlSnippet = list(map(getDescriptionFromResult, googleSearchResult))
        return convertor(htmlSnippet)
    except BaseException as error:
        print("Exception in extracting HTML : {}".format(error))
        return ""

    


def googleImageSearch(search):
    return getImageLink(googleSearch(search))

# test getLinkFromResult - PASS
# sampleResult = {'title': 'some title', 'link': "the link"}
# print(getLinkFromResult(sampleResult))

# test googe image search - PASS
print(
    getImageLink(
        googleSearch("caliburn", "image", num=1)
    )
)

# test googe text seatch - PASS
print(
    getDescription(
        googleSearch("caliburn", num=1)
    )
)