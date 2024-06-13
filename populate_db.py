from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from models import Base, Book, Author, Genre

DATABASE_URL = "postgresql://postgres:deepak@localhost:5432/bookstore"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def add_sample_data():
    db = SessionLocal()

    # Create sample authors
    author3 = Author(name="Author One", biography="Biography of Author One")
    author4 = Author(name="Author Two", biography="Biography of Author Two")

    db.add(author3)
    db.add(author4)
    db.commit()

    # Create sample genres
    genre3 = Genre(name="Fiction")
    genre4 = Genre(name="Non-Fiction")

    db.add(genre3)
    db.add(genre4)
    db.commit()

    # Create sample books
    book3 = Book(title="Book Three", author_id=author3.id, genre_id=genre3.id, publication_date=date(4043, 3, 3), price=39.99)
    book4 = Book(title="Book Four", author_id=author4.id, genre_id=genre4.id, publication_date=date(4043, 3, 4), price=49.99)

    db.add(book3)
    db.add(book4)
    db.commit()

    db.close()

if __name__ == "__main__":
    add_sample_data()
    print("Sample data added to the database.")
