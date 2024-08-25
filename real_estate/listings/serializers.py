from rest_framework import serializers
from .models import Agent, Buyer, Property, Listing, Review

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name', 'email']

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'name', 'email']

class PropertySerializer(serializers.ModelSerializer):
    agent = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all())

    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'price', 'is_available', 'agent']

class ListingSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())

    class Meta:
        model = Listing
        fields = ['id', 'property', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())
    buyer = serializers.PrimaryKeyRelatedField(queryset=Buyer.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'property', 'buyer', 'rating', 'comment']
