from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
<<<<<<< HEAD
=======
from .serializers import BookSerializer
>>>>>>> 663b29507509cf1a86de88479c843ea8b6e83afb


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
<<<<<<< HEAD
    data = []

    for book in books:
        data.append({
            "id": book.id,
            "title": book.title,
            "genre": book.genre
        })

    return Response(data)
=======
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
>>>>>>> 663b29507509cf1a86de88479c843ea8b6e83afb


@api_view(['POST'])
def ask_question(request):
<<<<<<< HEAD
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
=======
    question = request.data.get("question")

    books = Book.objects.all()[:5]

    context = ""
    sources = []

    for book in books:
        context += f"{book.title}: {book.summary}\n"
        sources.append(book.title)

    answer = f"Based on available books, here are some suggestions:\n\n{context}"
>>>>>>> 663b29507509cf1a86de88479c843ea8b6e83afb

    return Response({
        "question": question,
        "answer": answer,
<<<<<<< HEAD
        "sources": [book.title for book in filtered_books[:5]]
=======
        "sources": sources
>>>>>>> 663b29507509cf1a86de88479c843ea8b6e83afb
    })