
import requests

def get_poki_info(name):
    """
    Gets all info about a specified pokemon from poki api

    :param name: Pokemon name
    :returns: Dictionary of pokemon info, if successful. None if not
    """


    print("Getting pokimon information...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/' + name
    response = requests.get(URL)

    if response.status_code == 200:
        print('success')
        return response.json() #Convert response body to a dictionary
    else:
        print('failed. Response code:', response.status_code)
        return