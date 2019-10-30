
import random
import giphy_client
from giphy_client.rest import ApiException


giphy_token = INSERT_TOKEN_HERE
api_instance = giphy_client.DefaultApi()

def search_gifs(query):
    try:
        response = api_instance.gifs_search_get(giphy_token, 
            query, rating='g')
        lst = list(response.data)
        choice = random.randrange(25)
        print(choice)

        print(lst[choice].url)

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e
        
arg = input("Query: ")
search_gifs(arg)