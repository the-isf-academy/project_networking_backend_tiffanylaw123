# views.py

from banjo.urls import route_get, route_post
from .models import Recipe
from settings import BASE_URL

@route_get(BASE_URL + 'all')
def all_recipes(args):
    recipes_list = []

    for recipe in Recipe.objects.all()
        recipes_list.append(recipe.json_response())
    
    return {'recipe':recipes_list}

@route_post(BASE_URL + 'new', args={'cuisines':str, 'name':str, 'ingredients':str, 'instructions':str})
def new_recipe(args):
    new_recipe = Recipe(
        cuisines = args['cuisines'],
        name = args['name'],
        ingredients = args['ingredients'],
        instructions = args['instructions'],
        likes = 0,
        views = 0,
        popularity = 0
    )

    new_recipe.save()

    return {'recipe': new_recipe.json_response()}