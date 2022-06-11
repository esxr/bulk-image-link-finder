import pandas as pd

from image_search import getImageLink, googleSearch, googleImageSearch, getLinkFromResult, getDescription

def description(text):
    if(text):
        return getDescription(googleSearch(text, num=1))
        # return text
    raise Exception("No description found")

def image(text):
    if(text):
        return getImageLink(googleSearch(text, "image", num=3))
        # return text
    return Exception("No image found")


def filtered_data(filename):
    df = pd.read_csv(filename)

    # filter out rows with no description
    df = df[df["Name"].notnull()]
    df = df[df["Categories"].notnull()]

    return df

def main():
    df = filtered_data("in.csv")

    df['Images'] = df['Name'] + " " + df['Categories']
    df['Description'] = df['Name'] + " " + df['Categories']
    print(df.head(5))

    df["Images"] = df["Images"].apply(image)
    df["Description"] = df["Description"].apply(description)

    df.to_csv('out.csv', index=False)


if(__name__ == "__main__"):
    main()
