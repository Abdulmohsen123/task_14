# Your imports should be here
from rest_framework import routers, serializers, viewsets, views
from restaurants.models import *
from rest_framework.response import Response
# Complete me! I should be your APIListView
import requests
from django.http import Http404, JsonResponse

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name','opening_time','closing_time',)


# class RestaurantListView(viewsets.ModelViewSet):
class RestaurantListView(views.APIView):

	def get(self, request, format=None):
		restaurants = Restaurant.objects.all()
		serializer = RestaurantSerializer(restaurants, many=True)
		return Response(serializer.data)

def get_all_restaurants(request):
	url = "http://127.0.0.1:8000/api/list/"
	response = requests.get(url)
	print(response)
	return JsonResponse(response.json(), safe=False)