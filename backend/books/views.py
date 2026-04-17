from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    data = []

    for book in books:
        data.append({
            "id": book.id,
            "title": book.title,
            "genre": book.genre
        })

    return Response(data)


@api_view(['POST'])
def ask_question(request):
    question = request.data.get('question', '').lower()

    books = Book.objects.all()
    filtered_books = []

    for book in books:
       if any(word in book.title.lower() for word in question.split()) or \
   (book.genre and any(word in book.genre.lower() for word in question.split())):
            filtered_books.append(book)

    if not filtered_books:
        filtered_books = books[:5]

    answer = "Here are some relevant books:\n\n"

    for book in filtered_books[:5]:
        answer += f"{book.title} ({book.genre})\n"

    return Response({
        "question": question,
        "answer": answer,
        "sources": [book.title for book in filtered_books[:5]]
    })