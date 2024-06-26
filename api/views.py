from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import productSerializer
from .models import product

# Create your views here.


# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/product-list/',
#         'Detail View': '/product-detail/<int:id>',
#         'Create': '/product-create/',
#         'Update': '/product-update/<int:id>',
#         'Delete': '/product-delete/<int:id>',
#     }
#     return Response(api_urls)

@api_view(['GET'])
def productalllist(request):
    products = product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def productonelist(request, pk):
    products = product.objects.get(id=pk)
    serializer = productSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    serializer = productSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Create Operation Failed")


@api_view(['PATCH'])
def UpdateProduct(request, pk):
    products = product.objects.get(id=pk)
    serializer = productSerializer(instance=products, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response('Update Operation Failed')


@api_view(['DELETE'])
def DeleteProduct(request, pk):
    products = product.objects.get(id=pk)
    products.delete()
    return Response("Item Successfully Deleted")
