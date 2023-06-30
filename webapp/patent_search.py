import requests

def search_patent(patent_title):
    # Define the URL for the patent search API
    url = "https://api.patentsview.org/patents/query"

    # Define the query parameters
    params = {
        "q": {"_text_any": {"patent_title": patent_title}},
        "f": ["patent_title", "patent_year", "patent_abstract"]
    }

    # Make the HTTP request to the patent search API
    response = requests.get(url, params=params)

    # If the request was successful, return the results
    if response.status_code == 200:
        return response.json()["patents"]
    else:
        # If the request was not successful, raise an exception
        raise Exception("Patent search failed with status code {}".format(response.status_code))