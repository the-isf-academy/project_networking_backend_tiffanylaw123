# views.py

from banjo.urls import route_get, route_post
from .models import Recipe
from settings import BASE_URL

@route_get(BASE_URL + 'all')
def all_recipes(args):
    recipes_list = []

    for recipe in Recipe.objects.all():
        recipes_list.append(recipe.json_response())
    
    return {'recipes':recipes_list}

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

    return {'recipes': new_recipe.json_response()}

@route_get(BASE_URL + 'one', args={'id':int})
def one_recipe(args):
         
    if Recipe.objects.filter(id=args['id']).exists():
        one_recipe = Recipe.objects.get(id=args['id'])
        one_recipe.increase_views()
        return {'recipes':one_recipe.json_response()}
    
    else:
        return {'error': 'no recipes found'}

@route_post(BASE_URL + 'likes', args={'id':int})
def likes(args):
    if Recipe.objects.filter(id=args['id']).exists():
        likes = Recipe.objects.get(id=args['id'])
        likes.increase_likes()
        return {'recipes': likes.json_response()}
    else:
        return {'error': 'recipe doesnt exist'}

@route_get(BASE_URL + 'views', args={'id':int})
def views(args):
    if Recipe.objects.filter(id=args['id']).exists():
        views = Recipe.objects.get(id=args['id'])
        views.increase_views()
        return {'recipes': views.json_response()}
    else:
        return {'error': 'recipe doesnt exist'}

@route_post(BASE_URL + 'change_recipe', args={'id':int, 'new_recipe':str})
def change_recipe(args):
    if Recipe.objects.filter(id=args['id']).exists():
        change_recipe = Recipe.objects.get(id=args['id'])
        change_recipe.change_recipe(args['new_recipe'])
        return {'recipes': change_recipe.json_response()}
    else:
        return {'error': 'recipe doesnt exist'}

@route_get(BASE_URL + 'all/cuisines', args={'search_cuisines':str})
def different_cuisines(args):
    if Recipe.objects.filter(cuisines=(args['search_cuisines'])).exists:
        cuisines = Recipe.objects.filter(cuisines=(args['search_cuisines']))
        return {'recipe': cuisines.json_response()}
    
    else:
        return {'error': 'recipe doesnt exist'}


