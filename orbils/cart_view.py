from rest_framework import status
from rest_framework.views import APIView,Response
from .models import CartItem
from .serializers import ItemSerializer


class CartView(APIView):

    def get(self,request):
        items = CartItem.objects.all()
        items_data = ItemSerializer(items, many=True).data
        response_data = {"datas":items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        name = request.data.get('name')
        CartItem.objects.create(name=name)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self,request):
        name = request.data.get('name')
        item = CartItem.objects.filter(name=name).first()
        if item is None:
            response_data = {"response":"item doesn't exits"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.delete()
        response_data = {"response":"item deleted"}
        return Response(response_data,status=status.HTTP_200_OK)
