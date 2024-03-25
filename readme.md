# Meal Planner AI Model Service

## Overview

This repository is dedicated to the AI component of the Meal Planner Application, a powerful tool aimed at enhancing the meal planning process. Our service leverages a K-Nearest Neighbors (KNN) algorithm, implemented using Scikit-learn, to offer personalized recipe recommendations. These suggestions are made based on users' favorite recipes, dietary preferences, and restrictions, ensuring a customized meal planning experience. The backend is built with FastAPI, providing a responsive and scalable API for interaction with the AI model. Recipe data and user preferences are stored and managed within a MongoDB database, facilitating dynamic and real-time recommendations.

### Features

- **Personalized Recipe Recommendations:** Leverages a KNN algorithm to suggest recipes based on the user's favorite meals and dietary needs.
- **FastAPI Backend:** Utilizes FastAPI for a robust and efficient serving of AI model predictions.
- **Scikit-learn KNN Model:** Employs the KNN algorithm for predicting user preferences and suggesting personalized meal options.
- **MongoDB Database Integration:** Uses MongoDB for storing recipes and user preference data, enabling effective query performance for recommendations.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or later
- MongoDB
- FastAPI
- Uvicorn (for serving the FastAPI application)
- Scikit-learn
- Pandas (for data manipulation)

### Installation

1. **Clone the Repository:**
   Clone this repository to your local machine to get started with the AI model service.
   ```bash
   git clone https://github.com/yourrepository/mealplanner-ai-model.git
   python3 -m venv venv
   source venv/bin/activate
2. **Install dependencies:**
    pip install fastapi uvicorn scikit-learn pandas pymongo
3. **Start the application:**
    uvicorn main:app --reload

### License
This project is licensed under the MIT License 