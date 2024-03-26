from sklearn.neighbors import NearestNeighbors

class RecipeRecommender:
    def __init__(self, n_neighbors=3, metric='cosine'):
        self.knn_model = NearestNeighbors(n_neighbors=n_neighbors, metric=metric)
        self.recipes = None
        self.X_cv = None

    def fit(self, X_cv, recipes):
        self.knn_model.fit(X_cv)
        self.recipes = recipes
        self.X_cv = X_cv

    def get_recommendations(self, title):
        if self.recipes is None or self.X_cv is None:
            raise ValueError("Model and data not fitted.")
            
        recipe_index = self.recipes.index[self.recipes['title'] == title].tolist()[0]
        _, indices = self.knn_model.kneighbors(self.X_cv[recipe_index].reshape(1, -1))

        recommendations = []
        for i in indices.flatten():
            if i != recipe_index:
                recommended_title = self.recipes.at[i, 'title']
                allergies = self.recipes.at[i, 'allergies']
                recommendation = {"title": recommended_title, "allergies": allergies}
                recommendations.append(recommendation)

                return recommendations

        return