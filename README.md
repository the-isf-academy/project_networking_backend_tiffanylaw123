# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview

My API is a cooking recipe where people can collaborate and share different recipes. There are many features in this API, which include knowing the cuisine, name, ingredients needed and the instructions on how to many the recipe. You will also be able to see the amount of likes and views of each recipe and the amount of time it would take to make it. 

### Model

|      method name     | included field names |       field data type       |            parameter            |
|:--------------------:|:--------------------:|:---------------------------:|:-------------------------------:|
|     json_response    |         'id',        |             n/a             |               self              |
|                      |      'cuisine',      |    cuisine=StringField(),   |                                 |
|                      |        'name',       |     name=StringField(),     |                                 |
|                      |     'time taken'     |  time_taken=StringField(),  |                                 |
|                      |    'ingredients',    |  ingredients=StringField(), |                                 |
|                      |    'instructions'    | instructions=StringField(), |                                 |
|                      |       'likes',       |    likes=IntegerField(),    |                                 |
|                      |       'views',       |    views=IntegerField(),    |                                 |
|                      |     'popularity'     |   popularity=FloatField()   |                                 |
|                      |                      |                             |                                 |
|    increase_likes    |        'likes'       |     likes=IntegerField()    |               self              |
|                      |                      |                             |                                 |
|    increase_views    |        'views'       |     views=IntegerField()    |               self              |
|                      |                      |                             |                                 |
|     change_recipe    |    'ingredients',    |  ingredients=StringField(), | self, ingredients, instructions |
|                      |    'instructions'    | instructions=StringField(), |                                 |
|                      |       'likes',       |    likes=IntegerField(),    |                                 |
|                      |                      |                             |                                 |
| calculate_popularity |     'popularity'     |   popularity=FloatField()   |               self              |
|                      |       'likes',       |    likes=IntegerField(),    |                                 |
|                      |        'views'       |     views=IntegerField()    |                                 |

### Endpoints

|     route name     | HTTP method |          payload         |
|:------------------:|:-----------:|:------------------------:|
|     all_recipes    |     get     |            n/a           |
|                    |             |                          |
|     new_recipe     |     post    |      'cuisine':str,      |
|                    |             |        'name':str,       |
|                    |             |     'time_taken':str,    |
|                    |             |    'ingredients':str,    |
|                    |             |    'instructions':str    |
|                    |             |                          |
|     one_recipe     |     get     |         'id':int         |
|                    |             |                          |
|        likes       |     post    |         'id':int         |
|                    |             |                          |
|        views       |     get     |         'id':int         |
|                    |             |                          |
|    change_recipe   |     post    |         'id':int,        |
|                    |             |  'new_ingredients':str,  |
|                    |             |  'new_instructions':str  |
|                    |             |                          |
|    search_recipe   |     get     |    'keyword name':str    |
|                    |             |                          |
|   search/cuisines  |     get     |   'search cuisines':str  |
|                    |             |                          |
| search/ingredients |     get     | 'search ingredients':str |
|                    |             |                          |
|    quick_recipes   |     get     |            n/a           |
|                    |             |                          |
|     popularity     |     get     |         'id':int         |

---

## Setup

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



