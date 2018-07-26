# Your imports should be here
from rest_framework import routers, serializers, viewsets, views
from restaurants.models import *
from rest_framework.response import Response
# Complete me! I should be your APIListView


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