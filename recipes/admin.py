from django.contrib import admin

# Register your models here.
from recipes.models import Food, Ingredient, Recipe

admin.site.register(Food)
admin.site.register(Recipe)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('food', 'amount', 'measurement', 'recipe')

admin.site.register(Ingredient, IngredientAdmin)
