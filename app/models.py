# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Recipe(Model):
    cuisine = StringField()
    name = StringField()
    time_taken = IntegerField()
    ingredients = StringField()
    instructions = StringField()
    likes = IntegerField()
    views = IntegerField()
    popularity = FloatField()
    image = StringField()

    def json_response(self):
        
        return {
            'id': self.id,
            'cuisine': self.cuisine,
            'name': self.name,
            'time taken': self.time_taken,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'likes': self.likes,
            'views': self.views,
            'popularity': self.popularity
            'image': self.image
        }

    def increase_likes(self):       #is a method that will be used in views.py to increase likes
        self.likes += 1
        self.save()
    
    def increase_views(self):       #is a method that will be used in views.py to increase views
        self.views += 1
        self.save()

    def change_recipe(self, ingredients, instructions):     ##is a method that will be used in views.py to change recipe
        self.ingredients = ingredients
        self.instructions = instructions
        self.likes = 0
        self.save()

    def calculate_popularity(self):         #calculates the popularity of a recipe using likes/views * 100 so that the result would always be a full number
        self.popularity = (self.likes/self.views) * 100
        self.save()