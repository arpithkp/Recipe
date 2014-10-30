from django.conf.urls import patterns, include, url
from django.contrib import admin
from recipes.views import FoodListView, FoodDetailView, FoodCreateView, RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, IngredientCreateView, IngredientDeleteView, FoodList, FoodDetail, RecipeList, RecipeDetail, IngredientAddandDelete

admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipes_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^food/$', FoodListView.as_view(), name='food-list'),
    url(r'^food/(?P<pk>\d+)$', FoodDetailView.as_view(), name='food-detail'),
    url(r'^food/create$', FoodCreateView.as_view(), name='food-create'),
    url(r'^$', RecipeListView.as_view(), name='recipe-list'),
    url(r'^create/$', RecipeCreateView.as_view(), name='recipe-create'),
    url(r'^(?P<slug>[-\w]+)$', RecipeDetailView.as_view(), name='recipe-detail'),
    url(r'^(?P<slug>[-\w]+)/update$', RecipeUpdateView.as_view(), name='recipe-update'),
    url(r'^(?P<slug>[-\w]+)/add_ingredient/$', IngredientCreateView.as_view(), name='ingredient-create'),
    url(r'^(?P<slug>[-\w]+)/remove_ingredient/(?P<pk>\d+)/$', IngredientDeleteView.as_view(), name='ingredient-delete'),
    url(r'^api/food/$', FoodList.as_view(), name='food-api-list'),
    url(r'^api/food/(?P<pk>[0-9]+)/$', FoodDetail.as_view(), name='food-api-detail'),
    url(r'^api/recipes/$', RecipeList.as_view(), name='recipe-api-list'),
    url(r'^api/recipes/(?P<pk>[0-9]+)/$', RecipeDetail.as_view(), name='recipe-api-detail'),
    url(r'^api/(?P<slug>[-\w]+)/add_ingredient/$', IngredientAddandDelete.as_view(), name='ingredient-api-create'),
    url(r'^api/(?P<slug>[-\w]+)/remove_ingredient/(?P<pk>\d+)/$', IngredientAddandDelete.as_view(), name='ingredient-api-delete'),




)
