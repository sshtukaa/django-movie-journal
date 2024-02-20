"Movie Journal" (Kinojournal) is a web application that allows users to keep track of the movies they have watched or want to watch. Users can add movies, edit information about them, mark movies as watched, or add them to a "watchlist". The application utilizes the OMDB API to fetch information about movies such as titles, descriptions, ratings, cover art, etc.

Features:

1. User registration and authentication.
2. Adding movies to the database from OMDB using title search or movie ID.
3. Viewing a list of added movies with their information.
4. Marking movies as watched or adding them to the "watchlist".
5. Adding movie information (e.g., ratings).
6. Searching for movies based on various criteria (e.g., genre, release year).
7. Simple interface using HTML, CSS, and JavaScript to enhance the user experience.
8. Interaction with the SQL database through Django ORM.

Technologies:

1. Django for building the web application and managing the database.
2. HTML, CSS, and JavaScript for developing the user interface.
3. OMDB API for fetching movie information.

To run the project on your local machine, follow these steps:

1. Install Python and Django.
2. Clone the project repository from GitHub.
3. Install dependencies by running pip install -r requirements.txt.
4. Create the SQLite database and perform migrations using python manage.py migrate.
5. Start the Django development server with python manage.py runserver.
6. Navigate to http://127.0.0.1:8000/ in your web browser to begin using "Movie Journal".

"Movie Journal" is a great way to organize your movie life and keep track of all the movies you want to watch or have already watched. Enjoy this available code for your project or personal use!
