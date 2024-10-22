# views.py

from banjo.urls import route_get, route_post
from .models import Recipe
from settings import BASE_URL

@route_get(BASE_URL + 'all')    #shows all recipes
def all_recipes(args):
    recipes_list = []

    for recipe in Recipe.objects.all():
        recipes_list.append(recipe.json_response())
    
    return {'recipes':recipes_list}

@route_post(BASE_URL + 'new', args={'cuisine':str, 'name':str, 'time taken':str, 'ingredients':str, 'instructions':str})    #creates a new recipe
def new_recipe(args):
    new_recipe = Recipe(
        cuisine = args['cuisine'],
        name = args['name'],
        time_taken = args['time taken'],
        ingredients = args['ingredients'],
        instructions = args['instructions'],
        likes = 0,
        views = 0,
        popularity = 0
    )

    new_recipe.save()

    return {'recipes': new_recipe.json_response()}

@route_get(BASE_URL + 'one', args={'id':int})       #will only output the chosen recipe
def one_recipe(args):
         
    if Recipe.objects.filter(id=args['id']).exists():
        one_recipe = Recipe.objects.get(id=args['id'])
        one_recipe.increase_views()
        return {'recipes':one_recipe.json_response()}
    
    else:
        return {'error': 'no recipes found'}

@route_post(BASE_URL + 'likes', args={'id':int})        #increases likes on chosen recipe
def likes(args):
    if Recipe.objects.filter(id=args['id']).exists():
        likes = Recipe.objects.get(id=args['id'])
        likes.increase_likes()
        return {'recipes': likes.json_response()}
    else:
        return {'error': 'recipe doesnt exist'}

@route_get(BASE_URL + 'views', args={'id':int})     #increases views on chosen recipe
def views(args):
    if Recipe.objects.filter(id=args['id']).exists():
        views = Recipe.objects.get(id=args['id'])
        views.increase_views()
        return {'recipes': views.json_response()}
    else:
        return {'error': 'recipe doesnt exist'}

@route_post(BASE_URL + 'change_recipe', args={'id':int, 'new_ingredients':str, 'new_instructions':str})     #changes the ingredients and instructions of chosen recipe
def change_recipe(args):
    if Recipe.objects.filter(id=args['id']).exists():
        recipe_change = Recipe.objects.get(id=args['id'])
        recipe_change.change_recipe(args['new_ingredients'], args['new_instructions'])
        return {'recipes': recipe_change.json_response()}
    else:
        return {'error': 'recipe doesnt exist'}

@route_get(BASE_URL + 'search_recipe', args={'keyword name':str})       #searches for a recipe by its name, will output a list of recipes with the keyword given
def search_recipe(args):
    keyword_name = []

    for recipe in Recipe.objects.filter(name__contains=(args['keyword name'])):
        keyword_name.append(recipe.json_response())
    return {'recipes': keyword_name}

@route_get(BASE_URL + 'search/cuisines', args={'search cuisines':str})      #searches for a recipe by its cuisine, will output a list of recipes with the said cuisine
def search_cuisines(args):
    different_cuisines = []

    for recipe in Recipe.objects.filter(cuisine__contains=(args['search cuisines'])):
        different_cuisines.append(recipe.json_response())
    return {'recipes': different_cuisines}

@route_get(BASE_URL + 'search/ingredients', args={'search ingredients':str})        #searches for a recipe by its ingredients, will output a list of recipes with the ingredient searched
def search_ingredients(args):
    keyword_ingredients = []

    for recipe in Recipe.objects.filter(ingredients__contains=(args['search ingredients'])):
        keyword_ingredients.append(recipe.json_response())
    return {'recipes': keyword_ingredients}

@route_get(BASE_URL + 'quick_recipes')      #sorts the recipes from least amount of time taken to most
def least_to_most(args):
    time_ranking = []

    for recipe in Recipe.objects.order_by('time_taken'):
        time_ranking.append(recipe.json_response())
    return {'recipes': time_ranking}

@route_get(BASE_URL + 'popularity', args={'id':int})        #shows the popularity of a recipe
def popularity(args):
    if Recipe.objects.filter(id=args['id']).exists():
        popularity = Recipe.objects.get(id=args['id'])
        popularity.calculate_popularity()
        return {'recipes': popularity.json_response()}
    else:
        return {'error': 'statement doesnt exist'}   

