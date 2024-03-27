import pymongo
import pandas as pd
import os
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from RecipeRecommender import RecipeRecommender
tfidf_vectorizer = TfidfVectorizer()

load_dotenv()
environment = os.getenv('ENVIRONMENT', 'local') 
env_file = f'.env.{environment}'
load_dotenv(dotenv_path=env_file)

# Get data
myclient = pymongo.MongoClient(os.getenv("MONGO_URI"))
mydb = myclient[os.getenv("DATABASE_NAME")]
mycol = mydb["recipes"]

recipes_data = list(mycol.find())
recipes_df = pd.DataFrame(recipes_data)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Clean and prepare data
recipes_df = recipes_df[['title','keywords','cuisine','description','type','ingredients','allergies']]
recipes_df = recipes_df[recipes_df['type'].isin(['Vegan'])]
recipes_df.reset_index(drop=True,inplace=True)
recipes_df.dropna(inplace= True)

recipes_df['keywords'] = recipes_df['keywords'].apply(lambda x: ' '.join(x))
recipes_df['ingredients'] = recipes_df['ingredients'].apply(lambda x: ' '.join(d['name'] for d in x))
recipes_df['combined_features'] = (
    recipes_df['title'] +
    ' ' +
    recipes_df['keywords'] +
    ' ' +
    recipes_df['cuisine'] +
    ' ' +
    recipes_df['description'] +
    ' ' +
    recipes_df['type'] +
    ' ' +
    recipes_df['ingredients']
)

recipes = recipes_df[['title','combined_features','allergies']]

# Vectorize data
X_cv = tfidf_vectorizer.fit_transform(recipes['combined_features'])

recipe_recommender = RecipeRecommender()
recipe_recommender.fit(X_cv, recipes)

joblib.dump(recipe_recommender, 'recipes_model_vegan.joblib')