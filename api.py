import requests

def get_summary_covid_by_country(country):


    url = "https://api.covid19api.com/dayone/country/{}".format(country)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()