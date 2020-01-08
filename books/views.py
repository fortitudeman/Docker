from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Books


class BookListView(LoginRequiredMixin, ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin,DetailView): 
    model = Books
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'