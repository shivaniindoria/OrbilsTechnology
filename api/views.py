from rest_framework import status 
from rest_framework.views import APIView, Response 
from api.models import item

class DumpItApi(APIView):
    def get(self,request):
        items = item.objects.all()
        response_data = {"datas":items}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        name=request.data.get('name')
        item.objects.create(name=name)
        response_data = {'response':'item created'}
        return Response(response_data,status=status.HTTP_200_OK)