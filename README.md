# Cooklist

## Project Overview

Cooklist is a content-sharing web application that allows users to share recipes, plan meals, and create shopping lists. This application features a Django REST Framework backend and a React frontend. The goal is to create an interactive platform where users can manage their culinary activities seamlessly.

## Features

- User registration and login
- Profile management
- Recipe CRUD operations (Create, Read, Update, Delete)
- Commenting on recipes
- Rating recipes
- Marking recipes as favorites
- Meal planning
- Generating shopping lists
- Filtering recipes by tags or dietary preferences
- Securing the application

## Project Structure

Cooklist/ ├── backend/ │ ├── api/ │ │ ├── migrations/ │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── serializers.py │ │ ├── tests.py │ │ ├── urls.py │ │ ├── views.py │ ├── backend/ │ │ ├── init.py │ │ ├── asgi.py │ │ ├── settings.py │ │ ├── urls.py │ │ ├── wsgi.py │ ├── profiles/ │ │ ├── migrations/ │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── serializers.py │ │ ├── tests.py │ │ ├── urls.py │ │ ├── views.py │ ├── .env │ ├── manage.py │ ├── Procfile │ ├── requirements.txt │ └── README.md └── frontend/

## User Stories

1. **User Registration and Login**
   - As a user, I want to register and log in to the application so that I can access my account.
   - Acceptance Criteria: Users can register, log in, and receive feedback for unsuccessful login attempts.

2. **View Recipes**
   - As a user, I want to view a list of available recipes so that I can find ideas for meals.
   - Acceptance Criteria: Users can see all recipes in a list format.

3. **Add Recipe**
   - As a user, I want to add my own recipes so that I can share them with others.
   - Acceptance Criteria: Users can fill out a form to add new recipes.

4. **Edit Recipe**
   - As a user, I want to edit my recipes so that I can update them with new information.
   - Acceptance Criteria: Users can edit their existing recipes.

5. **Delete Recipe**
   - As a user, I want to delete my recipes if I no longer want to share them.
   - Acceptance Criteria: Users can delete their recipes with confirmation.

6. **View Recipe Details**
   - As a user, I want to see the details of a specific recipe so that I can understand how to prepare it.
   - Acceptance Criteria: Users can click on a recipe to see its detailed view.

7. **Comment on Recipe**
   - As a user, I want to comment on recipes so that I can share my thoughts and feedback.
   - Acceptance Criteria: Users can add and view comments on recipes.

8. **Rate Recipe**
   - As a user, I want to rate recipes so that I can indicate my preference for them.
   - Acceptance Criteria: Users can give a rating to a recipe.

9. **Mark Recipe as Favorite**
   - As a user, I want to mark recipes as favorites so that I can easily find them later.
   - Acceptance Criteria: Users can mark and unmark recipes as favorites.

10. **Meal Planning**
    - As a user, I want to plan my meals for the week so that I can stay organized.
    - Acceptance Criteria: Users can create and view their meal plans.

11. **Generate Shopping List**
    - As a user, I want to generate a shopping list based on my meal plan so that I can easily shop for ingredients.
    - Acceptance Criteria: Users can create a shopping list from selected recipes.

12. **Filter Recipes by Tags or Dietary Preferences**
    - As a user, I want to filter recipes based on tags or dietary preferences so that I can find suitable options.
    - Acceptance Criteria: Users can filter recipes using various criteria.

13. **Profile Management**
    - As a user, I want to manage my profile so that I can update my information and preferences.
    - Acceptance Criteria: Users can view and edit their profile information.

14. **Secure the Application**
    - As a developer, I want to secure the application to protect user data.
    - Acceptance Criteria: The application implements security measures for user data.

15. **API Integration**
    - As a user, I want the frontend to interact seamlessly with the backend API.
    - Acceptance Criteria: The frontend can perform CRUD operations on the backend.

## Environment Variables

- `SECRET_KEY`: The secret key for Django.
- `DATABASE_URL`: The URL for connecting to the database.
- `CLOUDINARY_URL`: The URL for Cloudinary storage.

## Deployment

To deploy the application on Heroku:
1. Create a new Heroku app.
2. Set up the environment variables in Heroku.
3. Push the code to Heroku using Git.

## Getting Started

1. Clone the repository: `git clone https://github.com/yourusername/Cooklist.git`
2. Navigate to the backend directory: `cd Cooklist/backend`
3. Set up a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Run the server: `python manage.py runserver`

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
