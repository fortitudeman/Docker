from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Books
from django.db.models import Q

class BookListView(LoginRequiredMixin, ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView): 
    model = Books
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status' # new

class SearchResultListView(ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'books/search_result.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Books.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )