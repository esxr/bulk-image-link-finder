import pandas as pd

from image_search import googleSearch, googleImageSearch, getLinkFromResult, getDescription

def description(text):
    if(text):
        return getDescription(googleSearch(text))
        # return text
    raise Exception("No description found")

def image(text):
    if(text):
        return googleImageSearch(text)
        # return text
    return Exception("No image found")
    

df = pd.read_csv("in.csv")

 
df['Images'] = df['Name'] + " " + df['Categories']
df['Description'] = df['Name'] + " " + df['Categories']
print(df.head(5))

df['Images'] = df['Images'].apply(image)
df['Description'] = df['Description'].apply(description)
print(df.head(5))

df.to_csv('out.csv', index=False)