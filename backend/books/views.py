from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def ask_question(request):
    question = request.data.get("question")

    books = Book.objects.all()[:5]

    context = ""
    sources = []

    for book in books:
        context += f"{book.title}: {book.summary}\n"
        sources.append(book.title)

    answer = f"Based on available books, here are some suggestions:\n\n{context}"

    return Response({
        "question": question,
        "answer": answer,
        "sources": sources
    })