
# Django Book Web Application

This is a web application built with Django that allows users to view, add, edit, and delete books from a database. Users can also search for books by title or author.

## Getting Started
### Prerequisites
Before you can run this application locally, you will need to have the following installed on your computer:
- Python 3
- Django
- PostgreSQL (or another database of your choice)

### Installing
To install the application and its dependencies, follow these steps:
- Clone this repository to your local machine
- Navigate to the project directory:
    ```
    cd <project-directory>
    ```
- Install the required python packages:
    ```
    pip install -r requirements.txt
    ```
- Create a PostgreSQL database for the application and update the DATABASES setting in settings.py to point to your database. For example:
   ```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Books',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '',
      }
    }
   ```
- Create the database tables.
  ```
  python manage.py migrate
  ```
- Load the initial data into the database.
  ```
  python manage.py import_books /path/to/books.csv
  ```

## Usage

1. Start the development server.
  ```
  python manage.py runserver
  ```
2. Open your web browser and go to http://localhost:8000/ to view the home page.
3. To add a new book to the database, click the "Add Book" button on the home page and fill out the form.
4. To edit the details of a book, click the "Edit" button on the book details page and update the form.
5. To delete a book, click the "Delete" button on the book details page and confirm the deletion.
6. To search for a book by title or author, enter the search term in the search box on the home page and click the "Search" button.
