# Your imports should be here
from rest_framework import routers, serializers, viewsets, views
from restaurants.models import *
from rest_framework.response import Response
# Complete me! I should be your APIListView
import requests
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect


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
	#url = "http://127.0.0.1:8000/api/list/"
	url = "https://api.github.com/events"
	response = requests.get(url)
	print(response.json())
	items = response.json()
		
	context = {
		"github_events": items,
	}
	return render(request, 'list.html', context)