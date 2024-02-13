# views.py
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ItemList(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = Item.objects.all()
        stock_status = self.request.query_params.get('stock_status', None)
        if stock_status:
            queryset = queryset.filter(stock_status=stock_status)
        return queryset

class ItemCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ItemUpdateAPIView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'sku'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ItemDeleteAPIView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    lookup_field = 'sku'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)