# Bookstore Inventory Management API

## Overview

This project is a RESTful API for managing a bookstore inventory, built with FastAPI. It supports CRUD operations for books, authors, and genres.

## Setup Instructions

### Prerequisites

- Python 3.7+
- PostgreSQL
- virtualenv (optional, but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Make sure your PostgreSQL server is running and create a new database:

    ```sql
    CREATE DATABASE bookstore;
    ```

5. **Update the database URL:**

    Edit `database.py` to use your PostgreSQL credentials:

    ```python
    DATABASE_URL = "postgresql://correct_user:correct_password@localhost/bookstore"
    ```

6. **Initialize the database:**

    ```bash
    python init_db.py
    ```

7. **Run the application:**

    ```bash
    uvicorn main:app --reload
    ```

## API Usage Examples

### Books

- **Retrieve all books:**

    ```bash
    GET /books/
    ```

- **Retrieve a specific book:**

    ```bash
    GET /books/{book_id}
    ```

- **Create a new book:**

    ```bash
    POST /books/
    {
        "title": "New Book",
        "author_id": 1,
        "genre_id": 1,
        "publication_date": "2024-06-12",
        "price": 19.99
    }
    ```

- **Update a book:**

    ```bash
    PUT /books/{book_id}
    {
        "title": "Updated Book",
        "author_id": 1,
        "genre_id": 1,
        "publication_date": "2023-06-12",
        "price": 24.99
    }
    ```

- **Delete a book:**

    ```bash
    DELETE /books/{book_id}
    ```

### Authors

- **Retrieve all authors:**

    ```bash
    GET /authors/
    ```

- **Retrieve a specific author:**

    ```bash
    GET /authors/{author_id}
    ```

- **Create a new author:**

    ```bash
    POST /authors/
    {
        "name": "New Author",
        "biography": "Biography of New Author"
    }
    ```

- **Update an author:**

    ```bash
    PUT /authors/{author_id}
    {
        "name": "Updated Author",
        "biography": "Updated Biography"
    }
    ```

- **Delete an author:**

    ```bash
    DELETE /authors/{author_id}
    ```

### Genres

- **Retrieve all genres:**

    ```bash
    GET /genres/
    ```

- **Retrieve a specific genre:**

    ```bash
    GET /genres/{genre_id}
    ```

- **Create a new genre:**

    ```bash
    POST /genres/
    {
        "name": "New Genre"
    }
    ```

- **Update a genre:**

    ```bash
    PUT /genres/{genre_id}
    {
        "name": "Updated Genre"
    }
    ```

- **Delete a genre:**

    ```bash
    DELETE /genres/{genre_id}
    ```

## Testing Instructions

### Prerequisites

- pytest
- pytest-asyncio

### Installation

Install the testing dependencies:

```bash
pip install pytest pytest-asyncio
