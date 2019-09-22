from django.shortcuts import render
import datetime
from books.models import Book

def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    if pub_date:
        books = Book.objects.all().filter(pub_date=pub_date)
        pub_dates = list(Book.objects.values_list('pub_date', flat=True).order_by('pub_date'))
        pub_date_index = pub_dates.index(datetime.datetime.strptime(pub_date, '%Y-%m-%d').date())
        prev_page = pub_dates[pub_date_index - 1] if pub_date_index else None
        next_page = pub_dates[pub_date_index + 1] if pub_date_index < len(pub_dates) - 1 else None

        context = {'books': books,
                   'prev_page': prev_page,
                   'next_page': next_page
                   }
    else:
        books = Book.objects.all()
        context = {'books': books}
    return render(request, template, context)
