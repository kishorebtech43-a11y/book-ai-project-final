import requests
from bs4 import BeautifulSoup
from .models import Book
from openai import OpenAI

client = OpenAI(api_key="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")

def generate_summary(text):
    return f"This book titled '{text}' explores key themes and ideas. It provides engaging content and insights for readers."

def generate_genre(text):
    genres = ["Fiction", "History", "Science", "Romance", "Thriller"]
    return genres[hash(text) % len(genres)]

def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select(".product_pod")

    for book in books:
        title = book.h3.a["title"]
        book_url = "http://books.toscrape.com/" + book.h3.a["href"]

        rating_class = book.p["class"][1]
        rating_map = {
            "One": 1, "Two": 2, "Three": 3,
            "Four": 4, "Five": 5
        }
        rating = rating_map.get(rating_class, 0)

        description = "No description available"
        summary = generate_summary(title)
        genre = generate_genre(title)

        if not Book.objects.filter(title=title).exists():
            Book.objects.create(
                title=title,
                description=description,
                rating=rating,
                book_url=book_url,
                summary=summary,
                genre=genre
            )

    return "Books scraped successfully"
