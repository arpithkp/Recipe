from django.core.urlresolvers import reverse
from rest_framework import generics, mixins
from rest_framework.exceptions import APIException
from recipes.models import Food, Recipe, Ingredient
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from recipes.serializer import RecipeSerailizer, FoodSerializer, IngredientSerailizer


class FoodListView(ListView):
    model = Food


class FoodDetailView(DetailView):
    model = Food


class FoodCreateView(CreateView):
    model = Food

class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe



class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = "recipes/recipe_update_form.html"


class IngredientCreateView(CreateView):
    model = Ingredient

    def get_initial(self, *args, **kwargs):
        recipe = Recipe.objects.get(slug=self.kwargs['slug'])
        return {'recipe': recipe}

    def get_success_url(self):
       return reverse('recipe-detail', args=[self.kwargs['slug']])


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'recipes/ingredient_confirm_delete.html'

    def get_success_url(self):
        return reverse('recipe-detail', args=[self.kwargs['slug']])



class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerailizer

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class RecipeDetail(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerailizer

class FoodDetail(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FunctionalityNotImplemented(APIException):

    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'

class IngredientAddandDelete(generics.ListCreateAPIView,generics.DestroyAPIView,FunctionalityNotImplemented):
    serializer_class = IngredientSerailizer
    queryset = Ingredient.objects.all()

