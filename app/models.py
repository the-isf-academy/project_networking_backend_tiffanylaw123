# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Recipe(Model):
    cuisines = StringField()
    name = StringField()
    ingredients = StringField()
    instructions = StringField()
    likes = IntegerField()
    views = IntegerField()
    popularity = FloatField()

    def json_response(self):
        
        return {
            'id': self.id,
            'cuisines': self.cuisines,
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'likes': self.likes,
            'views': self.views,
            'popularity': self.popularity
        }

    def increase_likes(self):
        self.likes += 1
        self.save()
    
    def increase_views(self):
        self.views += 1
        self.save()

    def change_recipe(self, ingredients, instructions):
        self.ingredients = ingredients
        self.instructions = instructions
        self.likes = 0
        self.save()

    def calculate_popularity(self):
        self.popularity_percentage = (self.likes/self.views) * 100
        self.save()