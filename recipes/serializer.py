from django.forms import widgets
from rest_framework import serializers, mixins
from recipes.models import Food, Recipe, Ingredient
from rest_framework import generics


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id','name')


class RecipeSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields  = ('id','title', 'slug', 'description')


class IngredientSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','recipe', 'food','amount','measurement')


