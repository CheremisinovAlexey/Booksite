from django.shortcuts import get_object_or_404, render

from .models import Book


def index(request):
    latest_question_list = Book.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'polls/detail.html', {'book': book})


