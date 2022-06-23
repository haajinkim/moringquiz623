from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category,Item
from .serializers import CaregorySerializer
# Create your views here.

class CaretgoryView(APIView):
    def get(self,request,categroy_id):
        categorys = Category.objects.filter(id=categroy_id)
        return Response(CaregorySerializer(categorys,many=True).data ,status=status.HTTP_200_OK)
    def post (self,request):
        name = request.data.get('name', '') 
        image_url = request.data.get('image_url', '')
        category = request.data.get('category','')
        print(name,image_url,category)
        new_article = Item.objects.create(
            name = name,
            image_url = image_url,
            category= category
        )
        category= Category.objects.get_or_create(name=category)
        # new_article.category.add(*category)
        new_article.save()
        return Response(status=status.HTTP_200_OK)   