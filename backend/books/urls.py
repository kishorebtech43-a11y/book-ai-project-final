from django.urls import path
from .views import get_books, ask_question

urlpatterns = [
    path('books/', get_books),
    path('ask/', ask_question),
]