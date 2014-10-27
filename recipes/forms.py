"""
@copyright: Copyright (c) 2014 Rackspace US, Inc.
"""
from django.core.urlresolvers import reverse

from django.forms import ModelForm, HiddenInput
from recipes.models import Ingredient

class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        widgets = {'recipe': HiddenInput()}

    #def get_success_url(self):
    #    return reverse('recipe-detail', args=[self.kwargs['slug']])
