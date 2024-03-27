from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import subprocess
import random

app = FastAPI()

recommender_vegan = joblib.load('recipes_model_vegan.joblib')
recommender_gain_weight = joblib.load('recipes_model_gain-weight.joblib')
recommender_loss_weight = joblib.load('recipes_model_loss-weight.joblib')
recommender_normal = joblib.load('recipes_model_normal.joblib')

class PredictionRequest(BaseModel):
    type: str
    favorite_recipes: list[str]
    allergens: list[str]

class Response(BaseModel):
    recipes: list[str]

def get_recipes(type: str, recipe: str) -> list:
    if type == 'Vegan' :
        return recommender_vegan.get_recommendations(recipe)
    elif type == 'Gain-weight' :
        return recommender_gain_weight.get_recommendations(recipe)
    elif type == 'loss-weight' :
        return recommender_loss_weight.get_recommendations(recipe)
    else :
        return recommender_normal.get_recommendations(recipe)
    
def validate_recipes(recipes: list, allergens: list) -> list:
    filtered_recipes = [
        recipe for recipe in recipes if not any(allergy in allergens for allergy in recipe['allergies'])
    ]

    unique_recipes = {recipe['title']: recipe for recipe in filtered_recipes}.values()
    validated_recipes = list(unique_recipes)

    return validated_recipes
         

@app.post('/api/get-suggestions', response_model=Response)
async def get_suggestions(request: PredictionRequest):
    suggested_recipes = []

    for recipe in request.favorite_recipes:
        recommendations = get_recipes(request.type, recipe)
        suggested_recipes.extend(recommendations)

    validated_recipes = validate_recipes(suggested_recipes, request.allergens)
    suggested_recipes_names = [recipe['title'] for recipe in validated_recipes]
    suggested_recipes_names.extend(request.favorite_recipes)
    random.shuffle(suggested_recipes_names)
    
    return Response(recipes=suggested_recipes_names)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)