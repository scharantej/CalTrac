## Flask Application Design for Calorie Tracking

### HTML Files
- **index.html**: The main page where users can input their meals and calorie counts. It includes a form with fields for meal name, calories, and date.
- **history.html**: A page displaying a history of all meals logged, along with their calorie counts and dates.

### Routes
- **index**: The route associated with the **index.html** file. It serves the initial page where users enter their meals.
- **add_meal**: A POST route that handles form submissions from the **index.html** file. It extracts the meal information, stores it in a database, and redirects to the **history** page.
- **history**: The route connected to the **history.html** file. It queries the database to retrieve all logged meals and displays them on the page.