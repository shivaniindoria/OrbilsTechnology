# import json
# import requests

# def get_fun_fact(_):
#     # URL from where we will fetch the data
#     url = "https://uselessfacts.jsph.pl/random.json?language=en"
#     response = requests.request("GET", url)
#     data = json.loads(response.text)
#     useless_fact = data['text']

from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class RandomQuoteAPIView(APIView):
    def get(self, request):
        url = "https://api.quotable.io/random"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return Response({"content": data.get('content', 'No Quote available.')})
        else:
            return Response({"content": "Failed to fetch Quote."})

        # category = 'happiness'
        # api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        # response = requests.get(api_url, headers={'X-Api-Key': 'E/yOMwnAqUWkKMaaNj2T3A==xnPROPkkH3wXKneX'})
        # if response.status_code == requests.codes.ok:
        #     data = response.json()
        #     return Response({"quote": data.get('quote', 'No Quote available.')})
        # else:
        #     return Response({"quote": "Failed to fetch Quote."})

class FunFactAPIView(APIView):
    def get(self, request):
        url = "https://uselessfacts.jsph.pl/random.json?language=hn"
        # url = " http://numbersapi.com/random/trivia"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return Response({"text": data.get('text', 'No fun fact available.')})
        else:
            return Response({"text": "Failed to fetch fun fact."})