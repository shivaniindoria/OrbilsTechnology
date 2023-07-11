from rest_framework import status 
from rest_framework.views import APIView, Response 

class DumpItApi(APIView):
    def get(self,request):
        items = [
            'apple',
            'grapes',
            'mango'
        ]
        response_data = {"datas":items}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        response_data = {'response':'hello,it is a post method'}
        return Response(response_data,status=status.HTTP_200_OK)