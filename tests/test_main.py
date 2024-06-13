import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from models import Base, Book, Author, Genre
from main import app, get_db
from schemas import BookCreate, AuthorCreate, GenreCreate

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Utility function to create initial data
def create_initial_data(db):
    db.add(Author(id=1, name="Author One", biography="Biography of Author One"))
    db.add(Genre(id=1, name="Fiction"))
    db.commit()

@pytest.fixture(scope="module")
def setup_db():
    db = TestingSessionLocal()
    create_initial_data(db)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_book(setup_db):
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author_id": 1, "genre_id": 1, "publication_date": "2023-01-01", "price": 19.99}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

def test_read_books(setup_db):
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_read_book(setup_db):
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

def test_update_book(setup_db):
    response = client.put(
        "/books/1",
        json={"title": "Updated Test Book", "author_id": 1, "genre_id": 1, "publication_date": "2023-01-01", "price": 29.99}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Book"

def test_delete_book(setup_db):
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Book"

def test_create_author(setup_db):
    response = client.post(
        "/authors/",
        json={"name": "New Author", "biography": "Biography of New Author"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "New Author"

def test_read_authors(setup_db):
    response = client.get("/authors/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_read_author(setup_db):
    response = client.get("/authors/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Author One"

def test_update_author(setup_db):
    response = client.put(
        "/authors/1",
        json={"name": "Updated Author", "biography": "Updated Biography"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Author"

def test_delete_author(setup_db):
    response = client.delete("/authors/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Author"

def test_create_genre(setup_db):
    response = client.post(
        "/genres/",
        json={"name": "New Genre"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "New Genre"

def test_read_genres(setup_db):
    response = client.get("/genres/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_read_genre(setup_db):
    response = client.get("/genres/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Fiction"

def test_update_genre(setup_db):
    response = client.put(
        "/genres/1",
        json={"name": "Updated Genre"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Genre"

def test_delete_genre(setup_db):
    response = client.delete("/genres/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Genre"
